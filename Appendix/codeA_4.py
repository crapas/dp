def exponential(N):
  if N <= 0:
    return 1
  else:
    return exponential(N - 1) + exponential(N - 1)

print(exponential(10))
