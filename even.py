import sys

arg=int(sys.argv[1])

def is_odd(y):
    return  y % 2 == 1
result1=is_odd(arg)
print("Is odd:", result1)

def is_even(x):
    return  x % 2 == 0 

result1=is_even(arg)
print("Is even:", result1)

n = len(sys.argv)
print("Total arguments passed:", n)

print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:")
for i in range(1, n):
	print(sys.argv[i])


Sum = 0
for i in range(1, n):
	Sum = Sum + int(sys.argv[i])

print("\n\nResult:", Sum)




       
    

     

