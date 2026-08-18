# Q1 - Lists


roll_no = "12345678"

L = [int(digit) * 10 for digit in roll_no]


print("Original List:", L)


L.append(90)
print("After append(90):", L)  

L.insert(2, 50)
print("After insert(2, 50):", L) 
L.remove(50)
print("After remove(50):", L)  

removed_element = L.pop()
print("After pop():", L)  


L.sort()
print("Ascending order:", L)

L.sort(reverse=True)
print("Descending order:", L)


print("First three elements:", L[:3])
print("Last three elements:", L[-3:])


average = sum(L) / len(L)

greater_than_average = [x for x in L if x > average]

print("Average:", average)
print("Elements greater than average:", greater_than_average)

#Q2 - Tuples

roll_no = "12345678"

L = [int(digit) * 10 for digit in roll_no]

scores = tuple(L[:8])

print("Scores tuple:", scores)

highest = max(scores)
lowest = min(scores)

print("Highest score:", highest)
print("Index of highest score:", scores.index(highest))

print("Lowest score:", lowest)
print("Frequency of lowest score:", scores.count(lowest))

reversed_scores = list(reversed(scores))

print("Reversed tuple as list:", reversed_scores)

user_score = int(input("Enter a score to search: "))

if user_score in scores:
    print("First occurrence index:", scores.index(user_score))
else:
    print("Score not present")

try:
    scores[0] = 100
except TypeError as e:
    print("Error:", e)

first_score, second_score, *remaining_scores = scores

print("First score:", first_score)
print("Second score:", second_score)
print("Remaining scores:", remaining_scores)

#ques 3

import random

roll_no = 12345678

random.seed(roll_no)

numbers = [random.randint(100, 900) for _ in range(100)]

print("Random numbers:")
print(numbers)

odd_numbers = [x for x in numbers if x % 2 != 0]

print("\nOdd numbers:")
print(odd_numbers)
print("Count of odd numbers:", len(odd_numbers))

even_numbers = [x for x in numbers if x % 2 == 0]

print("\nEven numbers:")
print(even_numbers)
print("Count of even numbers:", len(even_numbers))

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

prime_numbers = [x for x in numbers if is_prime(x)]

print("\nPrime numbers:")
print(prime_numbers)
print("Count of prime numbers:", len(prime_numbers))

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

most_frequent_number = max(frequency, key=frequency.get)
most_frequent_count = frequency[most_frequent_number]

print("\nMost frequently occurring number:", most_frequent_number)
print("Number of occurrences:", most_frequent_count)

#ques 4 

roll_no = "12345678"

digits = [int(digit) for digit in roll_no]

A = {digit * 7 for digit in digits}
B = {digit * 9 for digit in digits}

print("Set A:", A)
print("Set B:", B)

union = A.union(B)

print("\nUnion of A and B:", union)

intersection = A.intersection(B)

print("Intersection of A and B:", intersection)

A_minus_B = A.difference(B)
B_minus_A = B.difference(A)

print("A - B:", A_minus_B)
print("B - A:", B_minus_A)

symmetric_difference = A.symmetric_difference(B)

print("Symmetric difference:", symmetric_difference)

print("Is A a subset of B?", A.issubset(B))
print("Is B a superset of A?", B.issuperset(A))

value = int(input("\nEnter a value to remove from set A: "))

A.discard(value)

print("Set A after discard:", A)

#ques 5

my_dict = {
    "name": "Agrim Mittal",
    "roll_no": "12345678",
    "branch": "CSE",
    "age": 20,
    "city": "Panchkula"
}

print("Original dictionary:")
print(my_dict)

my_dict["location"] = my_dict.pop("city")

print("\nAfter renaming city to location:")
print(my_dict)

my_dict["cgpa"] = 8.0

print("\nAfter adding CGPA:")
print(my_dict)

my_dict["age"] += 1

print("\nAfter increasing age by 1:")
print(my_dict)

dict_copy1 = my_dict.copy()

removed_branch = dict_copy1.pop("branch")

print("\nUsing pop():")
print(dict_copy1)
print("Removed value:", removed_branch)

dict_copy2 = my_dict.copy()

del dict_copy2["branch"]

print("\nUsing del:")
print(dict_copy2)

print("\nKey -> Value:")

for key, value in my_dict.items():
    print(f"{key} -> {value}")

if "email" in my_dict:
    print("\nEmail:", my_dict["email"])
else:
    print("\nEmail not present")

friend_dict = {
    "name": "Rahul",
    "roll_no": "87654321",
    "branch": "CSE",
    "age": 20,
    "location": "Chandigarh"
}

merged_dict = {**my_dict, **friend_dict}

print("\nMerged dictionary:")
print(merged_dict)

string_values = {
    key: value
    for key, value in my_dict.items()
    if isinstance(value, str)
}

print("\nKey-value pairs where value is a string:")
print(string_values) 

