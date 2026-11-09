#!/usr/bin/env python3
"""Create original Lampa Switch artwork for the NRO and loading screen."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def draw_icon(size):
    scale = 4
    s = size * scale
    im = Image.new("RGB", (s, s), (14, 17, 25))
    d = ImageDraw.Draw(im)
    # Warm halo on a dark, uncluttered tile.
    glow = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    g = ImageDraw.Draw(glow)
    g.ellipse((int(.20*s), int(.06*s), int(.80*s), int(.66*s)), fill=(255, 146, 31, 120))
    glow = glow.filter(ImageFilter.GaussianBlur(s // 9))
    im = Image.alpha_composite(im.convert("RGBA"), glow)
    d = ImageDraw.Draw(im)
    orange = (255, 163, 48, 255)
    gold = (255, 211, 121, 255)
    # A simple luminous lamp rather than an unlicensed copied logo.
    d.ellipse((int(.30*s), int(.16*s), int(.70*s), int(.56*s)), fill=orange)
    d.arc((int(.37*s), int(.22*s), int(.63*s), int(.47*s)), 190, 340, fill=gold, width=max(1, int(.022*s)))
    d.rounded_rectangle((int(.40*s), int(.52*s), int(.60*s), int(.59*s)), radius=int(.018*s), fill=(238, 123, 34, 255))
    d.rounded_rectangle((int(.43*s), int(.60*s), int(.57*s), int(.65*s)), radius=int(.02*s), fill=(243, 185, 80, 255))
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(.12*s))
    except OSError:
        font = ImageFont.load_default()
    d.text((s//2, int(.81*s)), "LAMPA", anchor="mm", font=font, fill=(245, 246, 250, 255), stroke_width=0)
    return im.convert("RGB").resize((size, size), Image.Resampling.LANCZOS)


root = Path(__file__).resolve().parent.parent
out = root / "upstream/gx/nx/icon.jpg"
out.parent.mkdir(parents=True, exist_ok=True)
draw_icon(256).save(out, "JPEG", quality=95, subsampling=0)
print(f"Created {out}")
