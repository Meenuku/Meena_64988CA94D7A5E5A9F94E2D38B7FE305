def fact(n):
  if n<=1:
    return 1
  else:
    n=n*fact(n-1)
    return n
n=int(input("enter number:"))
print("factorial of ",n,"is",fact (n))