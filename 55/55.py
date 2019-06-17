lych = 0
for i in range(10001):
  initial_value = str(i)
  pal_value = initial_value[::-1]

  for j in range(51):
      initial_value = str(int(initial_value) + int(pal_value))
      pal_value = initial_value[::-1]

      if initial_value == pal_value:
        break
  else:
      lych += 1

print(lych)