#!/usr/bin/env node
/**
 * VUB platform build.
 * The consolidated tree is already deployment-shaped, so the build simply copies
 * the public top-level items into dist/site/ (excluding dev tooling, docs,
 * node_modules, and the archived legacy subrepos) and strips any large media as a
 * safety net (except the explicit compact DL2 video manifest).
 * Output: dist/site/  (or the first CLI arg).
 */
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const SITE_ROOT = path.join(ROOT, process.argv[2] || path.join("dist", "site"));

// Fail the build on courses.json <-> courses/ drift before copying anything.
require("child_process").execFileSync(process.execPath, [path.join(__dirname, "check-courses.mjs")], { stdio: "inherit" });

// Public, deployable top-level items — everything a learner or teacher needs.
const PUBLISH = ["index.html", "404.html", "courses.json", "courses", "instructors", "shared", "assets"];

function rmrf(t) { if (fs.existsSync(t)) fs.rmSync(t, { recursive: true, force: true }); }

function copyRecursive(src, dest) {
  const st = fs.statSync(src);
  if (st.isDirectory()) {
    fs.mkdirSync(dest, { recursive: true });
    for (const e of fs.readdirSync(src)) copyRecursive(path.join(src, e), path.join(dest, e));
  } else if (st.isFile()) {
    fs.copyFileSync(src, dest);
  }
}

function walk(dir) {
  const out = [], stack = [dir];
  while (stack.length) {
    const cur = stack.pop();
    for (const e of fs.readdirSync(cur, { withFileTypes: true })) {
      const full = path.join(cur, e.name);
      if (e.isDirectory()) stack.push(full); else out.push(full);
    }
  }
  return out;
}

const missing = PUBLISH.filter((i) => !fs.existsSync(path.join(ROOT, i)));
if (missing.length) throw new Error(`Cannot build site. Missing: ${missing.join(", ")}`);

rmrf(SITE_ROOT);
fs.mkdirSync(SITE_ROOT, { recursive: true });
for (const item of PUBLISH) copyRecursive(path.join(ROOT, item), path.join(SITE_ROOT, item));

// Critical files that must survive the copy — fail loudly if a refactor ever drops them.
const REQUIRED_FILES = [
  "index.html", "courses.json",
  "shared/brand.css", "shared/shell.css", "shared/shell.js", "shared/text-size.js",
  "shared/progress.js", "shared/glossary.js",
  "assets/vub-usflag.svg", "assets/vub-seal-white.png",
  "assets/fonts/source-sans-3-latin-400-normal.woff2",
];
const missingBuilt = REQUIRED_FILES.filter((f) => !fs.existsSync(path.join(SITE_ROOT, f)));
if (missingBuilt.length) throw new Error(`Build incomplete. Missing in dist/site: ${missingBuilt.join(", ")}`);

// DL2 ships six compact reviewed videos. Keep only this explicit media manifest;
// all other course MP4/MP3/MOV working files retain the existing stripping policy.
const dl2Media = JSON.parse(fs.readFileSync(path.join(ROOT, "courses/digital-literacy-2/media/manifest.json"), "utf8"));
const crypto = require("crypto");
if (dl2Media.videos.length !== 6) throw new Error("DL2 requires six reviewed videos");
const allowedMedia = new Set();
for (const video of dl2Media.videos) {
  if (!/^courses\/digital-literacy-2\/media\/week-0[1-6]\.mp4$/.test(video.path)) throw new Error("Invalid DL2 video path");
  const file = path.join(ROOT, video.path);
  const hash = crypto.createHash("sha256").update(fs.readFileSync(file)).digest("hex");
  if (hash !== video.sha256) throw new Error("DL2 media hash mismatch: " + video.path);
  if (fs.statSync(file).size > 20 * 1024 * 1024) throw new Error("DL2 video exceeds 20 MB deployment budget");
  allowedMedia.add(video.path);
}
if (allowedMedia.size !== 6) throw new Error("DL2 video manifest contains duplicates");
// Safety net for every other media file.
let stripped = 0;
for (const f of walk(SITE_ROOT)) {
  const l = f.toLowerCase();
  if ((l.endsWith(".mp4") || l.endsWith(".mp3") || l.endsWith(".mov")) && !allowedMedia.has(path.relative(SITE_ROOT, f).split(path.sep).join("/"))) { fs.rmSync(f, { force: true }); stripped += 1; }
}

const pages = walk(SITE_ROOT).filter((f) => f.toLowerCase().endsWith(".html")).length;
console.log(`Built site: ${SITE_ROOT}`);
console.log(`  ${pages} HTML pages published.` + (stripped ? `  Stripped ${stripped} media file(s).` : ""));
