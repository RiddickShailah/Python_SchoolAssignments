#Task 1
def is_power_of(num,n,):
    if num == 0:
        return False
    if num == 1:
        return True
    if num % n != 0:
        return False
    return is_power_of(num//n,n)




print(is_power_of(0,5))
print(is_power_of(1,5))
print(is_power_of(27,3))
print(is_power_of(279936,6))
print(is_power_of(1000000,10))
print(is_power_of(1000000,9))

#Task 2
def tribonacciSequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return tribonacciSequence(n-1) + tribonacciSequence(n-2) + tribonacciSequence(n-3)

print(tribonacciSequence(0))
print(tribonacciSequence(1))
print(tribonacciSequence(2))
print(tribonacciSequence(6))
print(tribonacciSequence(10))
print(tribonacciSequence(33))
