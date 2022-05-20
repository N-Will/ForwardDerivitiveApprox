import math

def forward(f,x,inc,m):
    dec_places = len(str(inc))
    h = 1    
    fprime = (f(x+h)-f(x))/h
    eps = 1
    
    while eps >= .5*(10**(-m)) :  
        previous = fprime
        h = round(h - inc, dec_places)    
        if h == 0: 
            print("Failed to converge, increase increment")
            break
        else:
            current = (f(x+h)-f(x))/h  
            eps = abs((current - previous) / current) 
            fprime = current
            continue
    if h != 0:
        print("The derivative is approximately " + str(fprime) + " with " + str(m) + " signficant digits.  The change used was " + str(h))
        return fprime, h
    else:
        return fprime, h

forward(lambda x: math.e**x, .125, .0001, 5)
forward(lambda x: math.sin(x), math.pi / 12,.0001, 5)
forward(lambda x: math.cos(x), math.pi / 12,.0001, 5)
forward(lambda x: math.asin(x), -.125, .0001, 5)
forward(lambda x: math.acos(x), -.125, .0001, 5)
forward(lambda x: math.atan(x), -.125, .0001, 5)
    


def increment(f, x, m):
    n = 1
    inc = .1 * 10**n  
    fprime, h = forward(f, x, inc, m)  
    while h != 0:  
        n += 1
        inc = .1 * 10**n   
        fprime, h = forward(f, x, inc, m) 
    print("The derivative is approximately " + str(fprime) + " with " + str(m) + " signficant figures. The change used was " + str(h) + " and we needed our increment to go out to " + str(n) + " decimal places.")
    return fprime, h, n

increment(lambda x: math.e**x, .125, 5)
increment(lambda x: math.sin(x), math.pi / 12, 5)
increment(lambda x: math.cos(x), math.pi / 12, 5)
increment(lambda x: math.asin(x), -.125, 5)
increment(lambda x: math.acos(x), -.125, 5)
increment(lambda x: math.atan(x), -.125, 5)
