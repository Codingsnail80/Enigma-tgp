from PIL import Image, ImageSequence
from rich.console import Console
from rich.live import Live
from rich.text import Text
import time

console = Console()

gif = Image.open("dancingDuck.gif")

frames = []
for frame in ImageSequence.Iterator(gif):
    frame = frame.convert("L").resize((40, 20))  # grayscale, resize
    chars = " q#2@&-_=+'.,`"
    pixels = frame.getdata()

    text = "".join(chars[p * len(chars) // 256] for p in pixels)
    lines = [text[i:i+40] for i in range(0, len(text), 40)]
    frames.append(Text("\n".join(lines)))

with Live(console=console, refresh_per_second=10, screen=True) as live:
    while True:
        for frame in frames:
            live.update(frame)
            time.sleep(0.1)

