# c = int(input())
# d = int(input())

# if c > d:
#     print("c is greater than d")
# else:
#     print("d is greater than c")
# n = int(input("Enter a number: "))

# if n <= 1:
#     print("Not Prime")
# else:
#     is_prime = True

#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print("Prime")
#     else:
#         print("Not Prime")


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# largest = max(a, b, c)

# print("Maximum number is:", largest)

# n = int(input("Enter n: "))

# sum = 0

# for i in range(1, n + 1):
#     if i % 7 == 0 and i % 9 == 0:
#         sum += i

# print("Sum =", sum)
# n = int(input("Enter n: "))

# sum = 0

# for i in range(2, n + 1):
#     prime = True

#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             prime = False
#             break

#     if prime:
#         sum += i

# print("Sum of prime numbers =", sum)



# def add(a, b):
#     return a + b

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# result = add(num1, num2)

# print("Sum =", result)

# def prime(n):
#     if n <= 1:
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True


# num = int(input("Enter a number: "))

# if prime(num):
#     print("Prime")
# else:
#     print("Not Prime")

# def sum_odd(n):
#     total = 0
#     for i in range(1, n + 1):
#         if i % 2 != 0:
#             total += i
#     return total

# n = int(input("Enter a number: "))
# print("Sum of odd numbers =", sum_odd(n))

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def sum_prime(n):
#     total = 0
#     for i in range(2, n + 1):
#         if is_prime(i):
#             total += i
#     return total

# n = int(input("Enter a number: "))
# print("Sum of prime numbers =", sum_prime(n))

