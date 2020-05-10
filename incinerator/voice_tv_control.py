class VoiceCommand:
    __init__=lambda s,ch=[],c=0:vars(s).update(locals())
    d=lambda s:{'f':0,'l':-1,'n':(s.c+1)%len(s.ch),'p':s.c-1}
    __getattr__=lambda s,n:lambda a=0:vars(s).update({'c':s.d().get(n[0],a-1)})
    current_channel=lambda s:s.ch[s.c]
    is_exist=lambda s,n:r'YNeos'[not(str!=type(n)and n<len(s.ch)or n in s.ch)::2]