import sys

def collatz(number): 
    if number % 2 == 0:
        ret = number // 2
        print(ret)
        return ret
    else:
        ret = 3 * number + 1
        print(ret)
        return ret


n = input("enter a number: ")
try:
    n = int(n)
except ValueError:
    print("Try again with a valid number buddy.")
    sys.exit()

while n != 1:
    n = collatz(n)


