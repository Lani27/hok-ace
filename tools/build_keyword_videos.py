"""Burn reviewed English subtitles into the 13 official dictionary clips.

Requires FFmpeg/FFprobe on PATH and the original 1280x720 MP4 clips.
Usage: python tools/build_keyword_videos.py --originals /path/to/originals
Original filenames match the keys in keyword_subtitles.json, e.g. fleeting.mp4.
"""
import argparse
import json
from pathlib import Path
import subprocess
import tempfile

from beginner_content import KEYWORDS, keyword_video_slug

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'docs/assets/beginner-guide/keyword-videos'


def timestamp(seconds, ass=False):
    scale = 100 if ass else 1000
    ticks = round(seconds * scale)
    whole, fraction = divmod(ticks, scale)
    minutes, seconds = divmod(whole, 60)
    hours, minutes = divmod(minutes, 60)
    if ass:
        return f'{hours}:{minutes:02}:{seconds:02}.{fraction:02}'
    return f'{hours:02}:{minutes:02}:{seconds:02},{fraction:03}'


def probe(path):
    return json.loads(subprocess.check_output([
        'ffprobe', '-v', 'error', '-show_entries',
        'format=duration:stream=codec_type,width,height', '-of', 'json', str(path)
    ], text=True))


def build(originals, only=None):
    subtitles = json.loads((ROOT / 'tools/keyword_subtitles.json').read_text(encoding='utf-8'))
    expected = {keyword_video_slug(name) for name, _, _ in KEYWORDS}
    if set(subtitles) != expected:
        raise ValueError('Subtitle keys must match every dictionary keyword.')
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for name, _, _ in KEYWORDS:
        slug = keyword_video_slug(name)
        if only and slug != only:
            continue
        source = originals / f'{slug}.mp4'
        metadata = probe(source)
        duration = float(metadata['format']['duration'])
        video = next(s for s in metadata['streams'] if s['codec_type'] == 'video')
        if (video['width'], video['height']) != (1280, 720):
            raise ValueError(f'{source}: caption placement requires 1280x720 input.')
        cues = subtitles[slug]
        previous_end = 0
        for start, end, text in cues:
            if not previous_end <= start < end <= duration:
                raise ValueError(f'{slug}: invalid or overlapping subtitle timing.')
            if len(text.splitlines()) > 2 or any(len(line) > 43 for line in text.splitlines()):
                raise ValueError(f'{slug}: subtitle exceeds two short lines: {text}')
            previous_end = end
        # Hold captions through pauses, covering the original Chinese caption strip.
        timed = [(start, cues[i+1][0] if i+1 < len(cues) else duration, text)
                 for i, (start, _, text) in enumerate(cues)]
        srt = '\n\n'.join(f'{i+1}\n{timestamp(start)} --> {timestamp(end)}\n{text}'
                          for i, (start, end, text) in enumerate(timed)) + '\n'
        (OUTPUT / f'{slug}-en.srt').write_text(srt, encoding='utf-8')
        ass = '''[Script Info]
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Caption,Arial,30,&H00FFFFFF,&H00FFFFFF,&H00302115,&H00302115,0,0,0,0,100,100,0,0,1,1,0,5,24,24,0,1
Style: Notice,Arial,18,&H00ECDECA,&H00ECDECA,&H00302115,&H00302115,0,0,0,0,100,100,0,0,3,6,0,9,24,24,20,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''
        ass += f'Dialogue: 1,0:00:00.00,{timestamp(duration, True)},Notice,,0,0,0,,UNOFFICIAL ENGLISH SUBTITLES\n'
        for start, end, text in timed:
            text = text.replace('\n', r'\N')
            ass += f'Dialogue: 0,{timestamp(start, True)},{timestamp(end, True)},Caption,,0,0,0,,{{\\pos(652,604)}}{text}\n'
        target = OUTPUT / f'{slug}-en.mp4'
        with tempfile.TemporaryDirectory(prefix='hok-subtitles-') as temp:
            work = Path(temp)
            (work / 'captions.ass').write_text(ass, encoding='utf-8')
            subprocess.run([
                'ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', str(source),
                '-vf', 'drawbox=x=312:y=565:w=680:h=78:color=0x18253B:t=fill,ass=captions.ass',
                '-map', '0:v:0', '-map', '0:a:0', '-c:v', 'libx264', '-preset', 'medium',
                '-crf', '22', '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-movflags', '+faststart',
                '-metadata', f'title={name} - English subtitles',
                '-metadata', 'comment=Unofficial fan subtitles. Original video: Tencent HoK ACE beginner guide.',
                str(target)
            ], cwd=work, check=True)
        if abs(float(probe(target)['format']['duration']) - duration) > 0.15:
            raise ValueError(f'{slug}: rendered duration differs from the original.')
        print(f'{slug}: {duration:.1f}s, {len(timed)} captions, {target.stat().st_size / 1048576:.1f} MiB', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--originals', type=Path, required=True)
    parser.add_argument('--only', choices=[keyword_video_slug(n) for n, _, _ in KEYWORDS])
    args = parser.parse_args()
    build(args.originals.resolve(), args.only)
