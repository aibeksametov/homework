import random
#A = int(input("A="))
#B = int(input("B="))
#1
#print(list(range(A,B)))
#2
#if A<B:
#    print(list(range(A,B)))
#else:
#    print(list(range(B,A)))
#3
#if (B-1)%2==1:
#    print(list(range(B-1,A,-2)))
#if (B-1)%2==0:
#    print(list(range(B,A,-2)))
n = int(input("n="))
sum = 0
for i in range(1, n + 1):
    sum += i
for i in range(n - 1):
    sum -= random.randint(1, n)
print(sum)
