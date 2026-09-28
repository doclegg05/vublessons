// Exercise the real delivered players, all chapter controls and caption tracks.
const { chromium } = require('@playwright/test');
const { AxeBuilder } = require('@axe-core/playwright');
const fs = require('node:fs/promises');
const assert = require('node:assert/strict');

(async () => {
  const base = process.env.DL2_REVIEW_URL || 'http://127.0.0.1:3948';
  const out = 'docs/digital-literacy-2/review/narration-refresh';
  await fs.mkdir(out, { recursive: true });
  const manifest = JSON.parse(await fs.readFile('courses/digital-literacy-2/media/manifest.json'));
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1440, height: 1000 } });
  const page = await context.newPage();
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  const videos = [];
  try {
    for (let n = 1; n <= 6; n++) {
      const week = `week-${String(n).padStart(2, '0')}`;
      const chapters = JSON.parse(await fs.readFile(`courses/digital-literacy-2/media/${week}-chapters.json`));
      const media = manifest.videos[n - 1];
      await page.goto(`${base}/courses/digital-literacy-2/weeks/${week}/video-transcript.html`);
      await page.waitForFunction(() => document.querySelector('video').readyState >= 1);
      const duration = await page.locator('video').evaluate(v => v.duration);
      assert(Math.abs(duration - media.durationSeconds) < .1);
      await page.locator('.video-chapters summary').click();
      const buttons = page.locator('[data-video-seek]');
      assert.equal(await buttons.count(), 10);
      for (let i = 0; i < chapters.length; i++) {
        const button = buttons.nth(i);
        assert(Math.abs(Number(await button.getAttribute('data-video-seek')) - chapters[i].startSeconds) < .001);
        await button.focus();
        await button.press(i % 2 ? 'Space' : 'Enter');
        await page.waitForFunction(time => {
          const v = document.querySelector('video');
          return !v.seeking && v.paused && Math.abs(v.currentTime - time) < .15;
        }, chapters[i].startSeconds);
      }
      const playback = [];
      for (const chapter of [0, 4, 9]) {
        const seek = chapters[chapter].startSeconds + 2;
        await page.locator('video').evaluate(async (v, time) => {
          v.muted = true;
          v.textTracks[0].mode = 'showing';
          v.currentTime = time;
          await v.play();
        }, seek);
        await page.waitForFunction(time => document.querySelector('video').currentTime > time + .7, seek);
        const state = await page.locator('video').evaluate(v => ({
          time: v.currentTime, paused: v.paused, readyState: v.readyState,
          cues: v.textTracks[0].cues.length,
          activeCaptions: Array.from(v.textTracks[0].activeCues || [], c => c.text),
          decodedAudioBytes: v.webkitAudioDecodedByteCount ?? null,
          decodedVideoFrames: v.getVideoPlaybackQuality().totalVideoFrames
        }));
        assert(!state.paused && state.readyState >= 2 && state.cues >= 100);
        assert(state.decodedVideoFrames > 0 && state.activeCaptions.length > 0);
        if (state.decodedAudioBytes !== null) assert(state.decodedAudioBytes > 0);
        await page.locator('video').evaluate(v => v.pause());
        playback.push({ chapter: chapter + 1, ...state });
      }
      await page.locator('video').screenshot({ path: `${out}/${week}-playback.png` });
      videos.push({ week, duration, keyboardChapterSeeks: 10, playback });
      console.log(`${week}: 10 keyboard seeks, 3 playback/caption/audio-decode samples passed`);
    }
    await page.goto(`${base}/${out}/index.html`);
    // Relative poster paths can break when a static server removes index.html.
    // Exercise the actual gallery too, including its one-player-at-a-time rule.
    const galleryVideos = page.locator('video');
    assert.equal(await galleryVideos.count(), 6);
    const galleryPlayback = [];
    for (let i = 0; i < 6; i++) {
      const video = galleryVideos.nth(i);
      await video.evaluate(async v => {
        const poster = new Image(); poster.src = v.poster;
        await poster.decode();
        if (!poster.naturalWidth) throw new Error('Gallery poster is empty');
        v.muted = true; await v.play();
      });
      await page.waitForFunction(index => document.querySelectorAll('video')[index].currentTime > .7, i);
      assert.equal(await page.locator('video').evaluateAll(vs => vs.filter(v => !v.paused).length), 1);
      galleryPlayback.push({ week: i + 1, posterLoaded: true, playbackAdvanced: true });
    }
    // Capture the fresh review view, with posters and no media downloaded
    // until the reviewer chooses Play.
    await page.reload();
    await page.locator('video').evaluateAll(vs => Promise.all(vs.map(async v => {
      const poster = new Image(); poster.src = v.poster; await poster.decode();
    })));
    const desktop = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21aa']).analyze();
    await page.screenshot({ path: `${out}/gallery-desktop.png`, fullPage: true });
    await page.setViewportSize({ width: 390, height: 844 });
    const mobile = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21aa']).analyze();
    await page.screenshot({ path: `${out}/gallery-mobile.png`, fullPage: true });
    assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth));
    const report = { videos, galleryPlayback, pageErrors: errors, galleryAccessibility: {
      desktop: desktop.violations, mobile: mobile.violations
    }};
    await fs.writeFile(`${out}/playback-verification.json`, JSON.stringify(report, null, 2) + '\n');
    assert.equal(errors.length, 0);
    assert.equal(desktop.violations.length, 0);
    assert.equal(mobile.violations.length, 0);
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
