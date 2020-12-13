def computepay(h,r):
	if h <40:
		salary=h*r
		return salary
	else:
		salary=(h*r)+(h-40)*0.5*r
		return salary
hrs = input("Enter Hours:")
hrate= input("enter the hourly rate")
h=float(hrs)
r=float(hrate)
p = computepay(h,r)
print("Pay",p)
