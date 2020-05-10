def text_formatting(text: str, width: int, style: str) -> str:
    fmtfu = {
        'l' : lambda x: x,
        'c' : lambda x: x.center(width).rstrip(),
        'r' : lambda x: x.rjust(width),
        'j' : lambda x: (' ' * ((width - len(x)) // x.count(' ') + 1)).join(w +
                         ' ' * ((width - len(x))  % x.count(' ') > n)
                            for (n, w) in enumerate(x.split()))
        }

    fmtng = lambda x: [
        fmtfu['l' if style == 'j' and i == len(x) else style](x[:i]) +
        ('\n' + fmtng(x[i + 1:]) if i < len(x) else '')
        for i in [len(x) if len(x) <= width else x[:width + 1].rfind(' ')] ][0]

    return fmtng(text)