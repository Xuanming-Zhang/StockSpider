d={}
with open('text.txt','r') as fd:
    while True:
        line = fd.readline()
        if not line:break
        ind = line.find(':')
        k = line[:ind]
        v = line[ind+1:].strip()
        d[k]=v
print(d)
with open('answer.txt','w') as fd:
    fd.write(str(d))