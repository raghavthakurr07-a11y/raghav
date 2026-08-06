
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