COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

def lines(text): # can be improved with textwrap module?
    if len(text) <= 39:
        return [text] if text else []
    try:
        i = text.rindex(' ',0,40)
    except ValueError: # no space in text[:39], I cut the text.
        return [text[:39]] + lines(text[39:])
    else:
        return [text[:i]] + lines(text[i+1:])

def cowsay(text):
    #text = ' '.join(text.split()) # tested and longer than while loop.
    while ' '*2 in text: text = text.replace(' '*2, ' ')
    #text = re.sub(r'\s{2,}', ' ', text) # but I don't want to import re (and longer)
    text = lines(text)
    max_len = max(map(len, text)) # maximum length of lines
    border = lambda ch: ' ' + ch * (max_len + 2) # top/bottom lines
    if len(text)==1:
        res = [f'< {text[0]} >']
    else:
        N = len(text) - 2 # number of lines with text
        res = [' '.join([first, t.ljust(max_len, ' '), last])
               for t, first, last in zip(text, '/'+'|'*N+'\\', '\\'+'|'*N+'/')]
    res = ['', border('_')] + res + [border('-')]
    return '\n'.join(res) + COW