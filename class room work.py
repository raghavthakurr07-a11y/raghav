
#find factorial of a number

"""num=int(input("Enter a number: "))
factorial=1
for i in range(1, num + 1):
    factorial *= i
print("The factorial of", num, "is", factorial)"""

#reverse string using reversed function


"""text=input("enter a string: ")
for i in reversed(text):
    print(i)"""
    
      # reverse string using for loop
    
"""text=input("enter a string: ")
reversed_text=""
for i in text:
        reversed_text=i+reversed_text
print(reversed_text)"""

#find no of vowels in a string

"""text=input("enter a string: ")
vowels="aeiouAEIOU"
count=0
for i in text:
    if i in vowels:
        count += 1
print("The number of vowels in the string is:", count)"""

#largest number in a list

"""
numbers = [5, 2, 8, 1, 9]
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print("The largest number in the list is:", largest)"""

#smallest no in a list

"""numbers = [5, 2, 8, 1, 9]
smallest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n
print("The smallest number in the list is:", smallest)"""

#table of a number using for loop

"""num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
    
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")"""
    
#loop for printing numbers in pattern order

"""for i in range(6):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()"""
    
#loop for printing numbers in reverse order

"""i=1
while i <= 5:
        print(i)
        i=i + 1
        print("exit loop")"""
 
 #calculator 
    
"""a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
operator=input("Enter operator: ")
if operator=='+':
    print(a+b)
elif operator=='-':
    print(a-b)
elif operator=='*':
    print(a*b)
elif operator=='/':
        print(a/b)
else:
    print("Invalid operator")"""
    
#prime no and not, enter by the user 

"""num=int(input("Enter a number: "))
count = 0
for i in range(2, num+1):
    if num % i == 0:
        count=count + 1
if count ==2:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")"""
    
"""#fibonacci series
num=int(input("Enter a number: "))
a, b = 0, 1
for _ in range(num):
    print(a, end=" ")
    a, b = b, a + b """
    
#add two numbers using function

"""def add_numbers(a, b):
    return a + b """

# Example usage

"""result = add_numbers(5, 3)
print("The sum is:", result)"""

# reveerse a string plindrome or not

"""text=input("enter a string:")
reversed_text=text[::-1]
if text==reversed_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")"""
    
 #check prime or not
    
"""num = 5
count=0
for i in range (1,num+1) :
    if num% i==0:
     count=count+1
    if count ==2:
     print("prime")
else:
    print("not prime")
"""
#for loop for printing numbers in pattern order in reverse order

"""for i in range(1000, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()"""
    
#check prime or not using function

"""def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")"""