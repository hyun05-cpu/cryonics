#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Renders cinematic placeholder plates for the cryonics interactive.
Same filenames / same aspect ratios as the final photoreal assets,
so the real renders can be dropped in without touching index.html.
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img")
os.makedirs(OUT, exist_ok=True)

# name, (w,h), base colour, glow colour, glow centre (x,y) 0-1, glow radius, label
PLATES = [
    ("00-cover.jpg",     (2400, 1350), (6, 10, 14),   (118, 160, 186), (0.50, 0.55), 0.62, "00  COVER / FROSTED DEWAR"),
    ("01-facility.jpg",  (2400, 1350), (9, 14, 19),   (126, 158, 178), (0.50, 0.48), 0.78, "01  FACILITY INTERIOR"),
    ("02-capsule.jpg",   (2000, 2500), (7, 11, 16),   (140, 172, 196), (0.50, 0.42), 0.58, "02  BODY IN CAPSULE"),
    ("03-vessel.jpg",    (2400, 1350), (10, 13, 17),  (150, 178, 200), (0.38, 0.52), 0.66, "03  CRYOPROTECTANT / VESSEL"),
    ("04a-ice.jpg",      (2000, 2000), (8, 12, 18),   (168, 198, 218), (0.50, 0.50), 0.70, "04A  ICE CRYSTAL DAMAGE"),
    ("04b-vitrified.jpg",(2000, 2000), (8, 12, 18),   (120, 150, 172), (0.50, 0.50), 0.74, "04B  VITRIFIED CELL"),
    ("05-inverted.jpg",  (2000, 2500), (5, 8, 12),    (104, 140, 166), (0.50, 0.62), 0.66, "05  HEAD-DOWN DEWAR SECTION"),
    ("06-brain.jpg",     (2400, 1350), (6, 9, 13),    (132, 166, 190), (0.52, 0.50), 0.60, "06  BRAIN MICROSTRUCTURE"),
]

FONTS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
]


def load_font(size):
    for p in FONTS:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()


def render(name, size, base, glow, centre, radius, label):
    w, h = size
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    nx = (xx / w - centre[0]) * (w / max(w, h))
    ny = (yy / h - centre[1]) * (h / max(w, h))
    d = np.sqrt(nx * nx + ny * ny)

    # soft central light falloff
    g = np.clip(1.0 - (d / radius), 0.0, 1.0) ** 2.1

    # faint horizontal strata -> reads as cold volumetric light
    strata = 0.045 * np.sin(yy / h * np.pi * 7.0 + nx * 3.0)
    g = np.clip(g + strata * g, 0.0, 1.0)

    img = np.zeros((h, w, 3), dtype=np.float32)
    for c in range(3):
        img[..., c] = base[c] + (glow[c] - base[c]) * g * 0.62

    # vignette
    vx = (xx / w - 0.5) * 2.0
    vy = (yy / h - 0.5) * 2.0
    vig = np.clip(1.0 - 0.62 * (vx * vx + vy * vy), 0.25, 1.0)
    img *= vig[..., None]

    # film grain
    rng = np.random.default_rng(abs(hash(name)) % (2 ** 31))
    grain = rng.normal(0.0, 3.4, (h, w, 1)).astype(np.float32)
    img = np.clip(img + grain, 0, 255)

    out = Image.fromarray(img.astype(np.uint8), "RGB").filter(ImageFilter.GaussianBlur(0.6))

    # hairline frame + centred label, so a missing render is obvious but not ugly
    d2 = ImageDraw.Draw(out, "RGBA")
    m = int(min(w, h) * 0.045)
    d2.rectangle([m, m, w - m, h - m], outline=(201, 214, 222, 40), width=max(1, w // 1400))

    fs = max(16, int(min(w, h) * 0.022))
    f = load_font(fs)
    tw = d2.textlength(label, font=f)
    tx, ty = (w - tw) / 2, h / 2 - fs * 0.7
    d2.text((tx, ty), label, font=f, fill=(214, 228, 236, 132))

    sub = "placeholder \u2014 replace with photoreal render"
    fs2 = max(12, int(min(w, h) * 0.0135))
    f2 = load_font(fs2)
    tw2 = d2.textlength(sub, font=f2)
    d2.text(((w - tw2) / 2, ty + fs * 1.9), sub, font=f2, fill=(160, 182, 196, 92))

    path = os.path.join(OUT, name)
    out.save(path, "JPEG", quality=86, optimize=True, progressive=True)
    print(f"{name:22s} {w}x{h}  {os.path.getsize(path)/1024:7.1f} KB")


for p in PLATES:
    render(*p)

print("\ndone ->", OUT)
