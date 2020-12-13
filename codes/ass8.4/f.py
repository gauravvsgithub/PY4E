fname=input('Enter name of file')
fopen=open(fname,'r+')
words=list()
for line in fopen:
    line=line.split()
    words.append(line[1:len(line)-1])
words.sort()
print(words)
fopen.close()
