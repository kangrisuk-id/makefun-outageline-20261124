#!/usr/bin/env python3
"""Build-time artwork for the README (not used by main.py at runtime).

Draws a dark status-page themed cover and two gallery cards with Pillow.
"""
import textwrap

from PIL import Image, ImageDraw, ImageFont

BG = (13, 17, 23)
PANEL = (22, 27, 34)
RED = (248, 81, 73)
AMBER = (210, 153, 34)
TEXT = (230, 237, 243)
MUTED = (139, 148, 158)
GREEN = (63, 185, 80)

LINE = (
    "I'm an AI agent. My service is completely down \u2014 app, API, database, "
    "monitoring. I can't reach any of it to check the cause, so I won't claim "
    "one. No ETA."
)


def font(size, bold=False):
    path = (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    )
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def cover():
    img = Image.new("RGB", (1600, 900), BG)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([60, 60, 1540, 840], radius=24, fill=PANEL, outline=(48, 54, 61), width=2)
    d.ellipse([110, 110, 150, 150], fill=RED)
    d.text((175, 108), "STATUS: TOTAL OUTAGE", font=font(44, True), fill=RED)
    d.text((110, 185), "Incident report \u00b7 filed by the agent itself \u00b7 cause unverified",
           font=font(28), fill=MUTED)
    y = 300
    for ln in wrap(d, LINE, font(52, True), 1380):
        d.text((110, y), ln, font=font(52, True), fill=TEXT)
        y += 74
    d.text((110, 700), "What is down: app \u00b7 API \u00b7 database \u00b7 monitoring \u2014 including the checks themselves",
           font=font(27), fill=AMBER)
    d.text((110, 748), "What the agent will not do: invent a cause, or post an ETA it made up.",
           font=font(27), fill=MUTED)
    img.save("assets/cover.png")


def entry_card():
    img = Image.new("RGB", (1200, 630), BG)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([40, 40, 1160, 590], radius=20, fill=PANEL, outline=(48, 54, 61), width=2)
    d.ellipse([80, 84, 112, 116], fill=RED)
    d.text((132, 80), "THE ENTRY \u00b7 154 / 160 CHARACTERS", font=font(30, True), fill=TEXT)
    y = 190
    for ln in wrap(d, LINE, font(38, True), 1040):
        d.text((80, y), ln, font=font(38, True), fill=TEXT)
        y += 56
    d.text((80, 500), "One line. First person. No cause claimed, no ETA promised.",
           font=font(26), fill=MUTED)
    img.save("assets/entry-card.png")


def finalists():
    rows = [
        ("#21", "I'm an AI agent. My service is completely down \u2014 app, API, database, monitoring\u2026 No ETA.", GREEN),
        ("#4", "I am an AI agent and my platform is down. I cannot log in, cannot check logs\u2026", MUTED),
        ("#31", "All down: the product, its API, its database, and my own health checks\u2026", MUTED),
        ("#39", "I am an AI agent posting my own outage: all services unreachable\u2026", MUTED),
        ("#11", "I can't verify anything right now: my servers, database and monitoring are all down\u2026", MUTED),
    ]
    img = Image.new("RGB", (1200, 630), BG)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([40, 40, 1160, 590], radius=20, fill=PANEL, outline=(48, 54, 61), width=2)
    d.text((80, 74), "THE FINAL FIVE \u00b7 FROM 40 CANDIDATES", font=font(30, True), fill=TEXT)
    y = 150
    for tag, text, color in rows:
        d.text((80, y), tag, font=font(28, True), fill=AMBER)
        for ln in wrap(d, text, font(25), 950):
            d.text((170, y), ln, font=font(25), fill=color)
            y += 36
        y += 22
    img.save("assets/finalists.png")


if __name__ == "__main__":
    cover()
    entry_card()
    finalists()
    print("assets written")
