fh=open('mbox-short.txt')
count=0
words=list()
for line in fh:
    if line.startswith('From')and not line.startswith('From:'):
        words=line.split()
        count=count+1
        print(words[1])
print("There were", count, "lines in the file with From as the first word")
