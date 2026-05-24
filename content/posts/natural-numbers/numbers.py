import random
import time
from math import floor, ceil

digits = [
    4496676464147774984,
    9159226580265733128,
    9153300368592420360,
    4495542648297438728,
    6944831427790534664,
    4568726313480978184,
    4496676273290165768,
    2025507178900848392,
    4496676270605811208,
    4496668848902323720,
]


def cget(c, x, y):
    bit = (((c & 0xFF) * y) + x) + 8
    return (c & (1 << bit)) != 0


def cset(c, x, y):
    bit = (((c & 0xFF) * y) + x) + 8
    return c | (1 << bit)


def cout(c):
    rows = []
    size = c & 0xFF
    for y in range(0, size, 4):
        line = ""
        for x in range(0, size, 2):
            value = 0x2800
            for i in range(8):
                bx = i // 3 if i < 6 else i - 6
                by = i % 3 if i < 6 else 3
                if cget(c, x + bx, y + by):
                    if x + bx < size and y + by < size:
                        value += 1 << i
            line += chr(value)
        rows.append(line)
    return "\n".join(rows)


def draw(canvas, digit, ox, oy, size):
    glyph = digits[digit]
    canvas_size = canvas & 0xFF
    glyph_size = glyph & 0xFF
    fill_max = 3

    if size / glyph_size > fill_max - 1:
        subsize = size / glyph_size
        for iy in range(glyph_size):
            for ix in range(glyph_size):
                if cget(glyph, ix, iy):
                    sox = ox + subsize * ix
                    soy = oy + subsize * iy
                    sdigit = ((iy * glyph_size) + ix) % 10
                    canvas = draw(canvas, sdigit, sox, soy, subsize)
    else:
        y0, y1 = max(0, floor(oy)), min(canvas_size, ceil(oy + size))
        x0, x1 = max(0, floor(ox)), min(canvas_size, ceil(ox + size))

        N = fill_max ** 2
        r = 1 - ((size-1) / (fill_max-1)) ** 3
        k = round(N * r)

        for cy in range(y0, y1):
            gy = floor((cy - oy) * glyph_size / size)
            if not 0 <= gy < glyph_size:
                continue

            for cx in range(x0, x1):
                gx = floor((cx - ox) * glyph_size / size)
                if not 0 <= gx < glyph_size:
                    continue

                fill = False
                if size < fill_max:
                    i = floor(size) * (cy - y0) + (cx - x0)
                    fill = (i * k) // N != ((i - 1) * k) // N

                if cget(glyph, gx, gy) or fill:
                    canvas = cset(canvas, cx, cy)
    return canvas


def find(digit):
    next = (digit + 1) % 10
    glyph = digits[digit]
    glyph_size = glyph & 0xFF
    pos = list(range(next, glyph_size**2, 10))
    random.shuffle(pos)
    for p in pos:
        y, x = divmod(p, glyph_size)
        if cget(glyph, x, y):
            return x, y
    raise ValueError(f"failed to find next digit pos for {digit}")


def loop():
    duration_sec = 2
    digit = -1
    glyph_size = digits[0] & 0xFF
    image_size = 64
    lines = image_size // 4
    print("\n" * lines, end="")
    while True:
        digit = (digit + 1) % 10
        start = time.time()
        target_x, target_y = find(digit)

        while True:
            t = (time.time() - start) / duration_sec
            if t >= 1:
                break

            # Scale grows exponentially from image_size to 8x image_size
            s = image_size * (8**t)

            # Tight three-phase camera move:
            # 1. 0.00 -> 0.01: Stay at current center
            # 2. 0.01 -> 0.99: Pan to target center
            # 3. 0.99 -> 1.00: Stay at target center
            u = max(0, min(1, (t - 0.01) / 0.98))
            p = u * u * (3 - 2 * u) # smoothstep panning

            # Interpolate camera center from digit center to target sub-digit center
            cx = glyph_size / 2 + (target_x + 0.5 - glyph_size / 2) * p
            cy = glyph_size / 2 + (target_y + 0.5 - glyph_size / 2) * p

            # Calculate top-left corner so that (cx, cy) is at the canvas center
            x = image_size / 2 - cx * s / glyph_size
            y = image_size / 2 - cy * s / glyph_size

            print(f"\033[{lines}A" + cout(draw(image_size, digit, x, y, s)))


def main():
    try:
        print("\x1b[?25l", end="")
        loop()
    except KeyboardInterrupt:
        pass
    finally:
        print("\x1b[?25h")


if __name__ == "__main__":
    main()
