# Prime Number Checker

def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False

        return True

num = int(input("Enter a number to check Prime : "))
print(is_prime(num))
