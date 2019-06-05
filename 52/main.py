for i in range(1, 300000):
  for j in range(2,7):
    comb = j*i
    i_set, comb_set = set(str(i)), set(str(comb))
    if i_set == comb_set:
      continue
    else:
      break
  else:
    print(i)
