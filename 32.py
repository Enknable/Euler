import itertools
z=[]
x = list(set(itertools.permutations(range(1,10), 9)))
for i in x:
  k = ''.join(str(e) for e in i)
  for h in range(int(len(k)/2)):
    for j in range(7-h):
      if int(k[8-j:])/int(k[0:h+1]) == int(k[h+1:8-j]):
        #print("match")
        if int(int(k[8-j:])) in z:
          pass
        else:
          z.append(int(k[8-j:]))
        #print(k[0:h+1], k[h+1:8-j], k[8-j:])
print(sum(z))
