import re

def left_join(phrases):
    l = list(phrases);
    l = ','.join(l); 
    return re.sub('right', 'left', l);