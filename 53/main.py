import math
def choice(n,c):
  sums = math.factorial(n) / (math.factorial(c) * math.factorial(n - c))
  return sums
count = 0
n = 0
c = 0
for i in range(n, 101):
  for j in range(c, i):
    sums = choice(i,j)
    if sums > 10**6:
      count += 1

print(count)
#n! / r!(n-r)!,