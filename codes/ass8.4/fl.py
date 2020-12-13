fname=input('Enter name of file')
fopen=open(\Users\Gaurav V Sonawane\Desktop\ass8.4\romeo.txt
words=list()
for line in fopen:
    line=line.split()
    winf.append(line[1:len(line)-1])
words.sort()
print(words)
