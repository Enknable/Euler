max = 0
for i in range(100):
  for j in range(100):
    temp = sum(list(map(int, str(i**j))))
    if temp > max:
      max = temp

print(max)