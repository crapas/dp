def polynomial(N):
  for i in range(0, N):
    for j in range(0, N):
      print('%d ' % (i * j), end='')
    print()

polynomial(10)