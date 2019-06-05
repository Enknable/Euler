import itertools

q=[]
def isdiv(num):
  x = int(num[1:4])
  print(x)

for i in itertools.permutations(range(10)):
  z = ''.join(str(e) for e in i)
  
  if int(z[1:4])%2==0 and int(z[2:5])%3==0 and int(z[3:6])%5==0 and int(z[4:7])%7==0 and int(z[5:8])%11==0:
    if int(z[6:9])%13==0 and int(z[7:10])%17==0:
      q.append(int(z))
print(sum(q))