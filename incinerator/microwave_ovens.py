class MicrowaveBase:
    def __init__(self):self.time=0;
    def gr(self):self.time=(lambda:90*60 if self.time>90*60 else(0 if self.time<0 else self.time))();
class Microwave1(MicrowaveBase):x=0
class Microwave2(MicrowaveBase):x=1
class Microwave3(MicrowaveBase):x=2
class RemoteControl:
    def __init__(self, micro):self.micro=micro
    def set_time(self, text):self.micro.time=int(text[0:2])*60+ int(text[3:5])
    def add_time(self,text):
        self.micro.time+=(lambda a,j:int(text[:text.index(a)])*j)((lambda: "s" if "s" in text else "m")(),(lambda:1 if "s" in text else 60)())
        self.micro.gr()
    def del_time(self,text):
        self.micro.time-=(lambda a,j:int(text[:text.index(a)])*j)((lambda: "s" if "s" in text else "m")(),(lambda:1 if "s" in text else 60)()) 
        self.micro.gr()
    show_time=lambda self: (lambda a,b:"_"+b[1:] if a==0 else(b[:-1]+"_" if a==1 else b))(self.micro.x, str(self.micro.time//60).zfill(2)+":"+str(self.micro.time%60).zfill(2))