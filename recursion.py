#Write a recursive function to add the first n terms of the series:
#1 + 1/2 - 1/3 + 1/4 - 1/5 ...
def sumNTerm(n):
   if n > 1:
      if n % 2 == 0:
         return 1/n+sumNTerm(n-1)
      else:
         return -1/n+sumNTerm(n-1)
   else:
      return n
   
n = int(input("Enter the number of terms to sum:\n"))

print("Sum of first",n,"terms =", sumNTerm(n))

#Greatest Common Denominator
def GCD(n,m):
    if(m==0):
        return n
    else:
        return GCD(m,n%m)

n1 = int(input("Enter the first number:\n"))
n2 = int(input("Enter the second number:\n"))    

print("The GCD of", n1, "and", n2, "is", GCD(n1,n2))

#Tower of hanoi
def moveTower(height,fromPole, toPole, withPole):
   # add code here
   #call moveDisk in your function call.
    if height == 0:
        return
    moveTower(height-1, fromPole, withPole, toPole)
    moveDisk(fromPole, toPole)
    moveTower(height-1, withPole, toPole, fromPole)


def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

disks = int(input("Enter the number of disks:\n"))    
moveTower(disks,"A","B","C")