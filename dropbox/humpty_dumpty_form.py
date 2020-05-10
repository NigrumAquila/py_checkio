from cmath import pi, sqrt, log

def checkio(h, w):
    return (lambda h,w: [round(i.real, 2) for i in 
        (lambda h,w,m,e: (2*m*h/3, m + (pi*h**2/e*log((1+e)/(1-e)) if e else m))
        )(h, w, 2*pi*w**2, sqrt(1-(h**2)/(w**2)))
    ])(h/2, w/2)