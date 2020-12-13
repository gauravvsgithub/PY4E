import re
sumup=0
x=list()
fopen=open('regex_sum_406784.txt')
for line in fopen:
    line=line.rstrip()
    x = re.findall(('[0-9]+'),line)
    if len(x)<1:
        continue
    for i in x:
        sumup = sumup + int(i)
        
print(sumup)
