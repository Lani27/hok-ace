"""Apply individually reviewed lettering repairs to recreated image candidates.

Unlike automatic OCR overlays, each repair uses an explicit area and type size.
Run with --input-dir containing candidate-<folder>__<name>.png files. Requires
Pillow, NumPy, and OpenCV; approved image candidates are produced with ImageGen.
"""
import argparse
from io import BytesIO
import json
from pathlib import Path
import subprocess

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]


def render(source, operations):
    image = Image.open(source).convert('RGB')
    for item in operations:
        if item['kind'] == 'original':
            raw = subprocess.check_output(['git', 'show', item['revision'] + ':docs/assets/' + item['file']], cwd=ROOT)
            original = Image.open(BytesIO(raw)).convert('RGB')
            image.paste(original.crop(tuple(item['box'])), tuple(item['box'][:2]))
            continue
        if item['kind'] == 'insert':
            x0, y0, x1, y1 = item['box']
            insert = Image.open(ROOT / item['asset']).convert('RGB')
            image.paste(insert.resize((x1-x0, y1-y0), Image.Resampling.LANCZOS), (x0, y0))
            continue
        if item['kind'] == 'copy':
            image.paste(image.crop(tuple(item['source'])), tuple(item['destination']))
            continue
        x0, y0, x1, y1 = item['box']
        if item['kind'] == 'text':
            pixels = np.array(image)
            mask = np.zeros(pixels.shape[:2], dtype=np.uint8)
            cx0, cy0, cx1, cy1 = item.get('clear_box', item['box'])
            crop = pixels[cy0:cy1, cx0:cx1]
            gray = cv2.cvtColor(crop, cv2.COLOR_RGB2GRAY)
            selected = gray < item.get('threshold', 165)
            if item.get('light_text'):
                selected = gray > item.get('threshold', 165)
            if item.get('clear_rectangle'):
                selected[:] = True
            mask[cy0:cy1, cx0:cx1] = selected.astype(np.uint8) * 255
            mask = cv2.dilate(mask, np.ones((3, 3), np.uint8))
            image = Image.fromarray(cv2.inpaint(pixels, mask, 3, cv2.INPAINT_TELEA))
        draw = ImageDraw.Draw(image)
        if item['kind'] == 'label':
            draw.rectangle(item['box'], fill=item['background'])
        if item['kind'] == 'pill':
            draw.rounded_rectangle(item['box'], radius=20, fill=item['background'], outline='white', width=1)
        font = ImageFont.truetype('C:/Windows/Fonts/' + item.get('font', 'arial.ttf'), item['size'])
        bounds = draw.multiline_textbbox((0, 0), item['text'], font=font, spacing=2)
        text = Image.new('RGBA', (bounds[2]-bounds[0]+2, bounds[3]-bounds[1]+2))
        ImageDraw.Draw(text).multiline_text((1-bounds[0], 1-bounds[1]), item['text'], font=font, fill=item['color'], spacing=2)
        if item.get('rotate'):
            text = text.rotate(item['rotate'], expand=True)
        if text.width > x1-x0 or text.height > y1-y0:
            raise ValueError(f'Text exceeds reviewed area: {item["text"]}')
        x = x0 if item.get('align') == 'left' else x0 + (x1-x0-text.width)//2
        y = y0 + (y1-y0-text.height)//2
        image.paste(text, (x, y), text)
    return image


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-dir', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'docs/assets')
    parser.add_argument('--only')
    args = parser.parse_args()
    repairs = json.loads((ROOT / 'tools/image_lettering_repairs.json').read_text(encoding='utf-8'))
    for file, operations in repairs.items():
        if args.only and file != args.only:
            continue
        source = args.input_dir / ('candidate-' + file.replace('/', '__'))
        image = render(source, operations)
        destination = args.output_dir / file
        destination.parent.mkdir(parents=True, exist_ok=True)
        image.save(destination, optimize=True)
        print(file)


if __name__ == '__main__':
    main()
