import re, sys, textwrap

# viewport_w, viewport_h, center_x, center_y
CONFIG = {
    'level': (100, 25, 51, 25),
    'dream': (100, 20, 56.7, 0),
}

def main():
    filepath = sys.argv[1]
    content = open(filepath, 'r', encoding='utf-8').read()
    config = CONFIG[filepath.removesuffix('_clean.svg')]

    path_pattern = re.compile(r'<path\b[^>]*?(?:/?>.*?</path>|/?>)', re.DOTALL | re.IGNORECASE)
    paths = path_pattern.findall(content)

    w, h, x, y = config

    p = print

    padding = 5

    p(f'<svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" width="500" height="500" viewBox="{-padding} {-padding} {w+padding*2} {h+padding*2}">')

    p(f'<g transform-origin="{x} {y}">')

    p('<g>')
    for path in paths:
        p(path)
    p(textwrap.dedent('''\
        <animate
            attributeName="opacity"
            to="0"
            dur="5s"
            calcMode="spline"
            keySplines="0.5 0 1 1"
        repeatCount="indefinite"
        />
    '''))
    p('</g>')

    for i in range(10):
        p(f'<g transform="scale({1 / 2 ** (i+1)})" transform-origin="{x} {y}">')
        for path in paths:
            print(path)
        p('</g>')

    p(textwrap.dedent('''\
        <animateTransform
            attributeName="transform"
            type="scale"
            values="1; 2"
            dur="5s"
            keyTimes="0; 1"
            calcMode="spline"
            keySplines="0.5 0 1 1"
            repeatCount="indefinite"
        />
    '''))
    p('</g>')
    p('</svg>')


if __name__ == "__main__":
    main()
