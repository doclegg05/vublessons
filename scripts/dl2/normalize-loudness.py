"""Normalize delivered DL2 MP4 audio to one loudness target without touching the video stream.

Two-pass EBU R128 loudnorm (measure, then apply linear gain), AAC re-encode, faststart.
Usage: python3 scripts/dl2/normalize-loudness.py [--target -18] [--peak -1.5] [paths...]
Default paths: courses/digital-literacy-2/media/week-0[1-6].mp4 (rewritten in place via a temp file).
"""
import argparse,json,re,shutil,subprocess,sys,tempfile
from pathlib import Path
def measure(path,target,peak):
    log=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',str(path),'-af',f'loudnorm=I={target}:TP={peak}:LRA=11:print_format=json','-vn','-f','null','-'],capture_output=True,text=True).stderr
    return json.loads(log[log.rfind('{'):])
def integrated(path):
    log=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',str(path),'-af','ebur128','-vn','-f','null','-'],capture_output=True,text=True).stderr
    tail=log[log.rfind('Integrated loudness'):];return float(re.search(r'I:\s+(-?[0-9.]+) LUFS',tail).group(1))
def normalize(path,target,peak):
    m=measure(path,target,peak)
    if abs(float(m['input_i'])-target)<0.3 and float(m['input_tp'])<=peak+0.05:
        return dict(path=str(path),before=float(m['input_i']),after=float(m['input_i']),skipped=True)
    af=(f"loudnorm=I={target}:TP={peak}:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
        f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true:print_format=summary")
    with tempfile.NamedTemporaryFile(suffix='.mp4',delete=False,dir=path.parent) as tmp:out=Path(tmp.name)
    subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(path),'-map','0:v','-map','0:a','-c:v','copy','-af',af,'-ar','48000','-c:a','aac','-b:a','128k','-movflags','+faststart',str(out)],check=True)
    shutil.move(str(out),str(path))
    return dict(path=str(path),before=float(m['input_i']),after=integrated(path),skipped=False)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--target',type=float,default=-18.0);ap.add_argument('--peak',type=float,default=-1.5);ap.add_argument('paths',nargs='*')
    a=ap.parse_args();paths=[Path(p) for p in a.paths] or sorted(Path('courses/digital-literacy-2/media').glob('week-0[1-6].mp4'))
    results=[normalize(p,a.target,a.peak) for p in paths]
    for r in results:print(f"{Path(r['path']).name}: {r['before']:.1f} -> {r['after']:.1f} LUFS{' (already on target)' if r['skipped'] else ''}")
    spread=max(r['after'] for r in results)-min(r['after'] for r in results)
    print(f'spread {spread:.2f} LU');sys.exit(0 if spread<=1.0 else 1)
if __name__=='__main__':main()
