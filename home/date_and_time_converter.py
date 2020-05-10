import calendar

def date_time(time: str) -> str:
    time=time.split()
    D,M,Y=time[0].split(".")
    M,D=calendar.month_name[int(M)],str(int(D))
    h,m=(str(int(x)) for x in time[1].split(":"))
    return " ".join((D,M,Y,"year",h,"hour"+"s"*(h!="1"),m,"minute"+"s"*(m!="1")))