import re

def checkio(text):
    return re.sub('\$\d{1,3}(\.\d{3})*(,\d{2}){,1}(?!\d)',
        lambda x: x.group(0).translate(str.maketrans(',.', '.,')), text)