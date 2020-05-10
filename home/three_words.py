import re

def checkio(words: str) -> bool:
    count = 0;
    l = words.split(' ');
    for key in l:
        bu = False;
        asd = re.match(r'[0-9]', key)
        if(asd != None and len(asd.group(0)) != 0):
            bu = True;
        if(bu):
            count = 0;
        else:
            count += 1;
        if(count == 3):
            return True;
            
    return False;