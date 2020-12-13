def computepay(h,r):
    if h>40 :
        return 40*10.5+(h-40)*10.5*1.5
    else :
        return (h)*10.5
    #return ((h>40)?40*10.5+(h-40)*10.5*1.5:(h)*10.5)

hrs = input("Enter Hours:")
h=float(hrs)
rate=input("Enter Rate:")
r=float(rate)
p = computepay(h,r)
print("Pay",p)
