import sys
SECRET_KEY = "sfdwa87wq37"
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
  
def div(n):
    res=10/n
    return res
  
def main(n):
    res=fact(n)
    print(res)
  
if __name__=="__main__":
    if len(sys.argv)>1:
        main(int(sys.argv[1]))
class A:
    def __mul__(self, other, unexpected):  # Noncompliant. Too many parameters
        return 42

    def __add__(self):  # Noncompliant. Missing one parameter
        return 42
