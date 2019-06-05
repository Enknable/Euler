a = open("file1.txt", "r")
tn = []
y=[]
count = 0
for i in a:
  x = i.split(",")
for i in x:
  z = i.replace("\"", "")
  q=0
  for j in z:
    q += ord(j) - 64
    #print(j, ord(j)-64)
  y.append(q)
    
for i in range(10000):
  tn.append(int(0.5*i*(i+1)))

for i in y:
  if i in tn:
    #print(i)
    count += 1
    
print(count)