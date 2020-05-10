import re;

def find_message(text: str) -> str:
    if(0 < len(text) <= 1000):
        secret = "";
        s = re.findall('([A-Z])', text);
        secret = secret.join(s);
    return secret;