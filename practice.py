#Accept an integer and print Hello world that times
a = int(input("Enter any integer number: "))


for i in range(1,a+1):
    print("Hello world")










#Print natural numbers upto n
a = int(input("Please give an number: "))
print(f"natural number upto {a} are following: ")

for i in range(1,a+1):
    print(i)










# Take an natural number and print reverse to 1

a = int(input("Please give an number: "))
print("The number in the reverse order are following: ")

for i in range(a,0,-1):
    print(i)










#Take a number in input and print its table

a = int(input("Please enter an number: "))
print(f"Table of {a} is following : ")

for i in range(1,11):
    print(f"{a} * {i} = {a*i}")








# Take an input from the user and print the sum upto that term

a = int(input("Please enter your number: "))
jod = 0

for i in range(1,a+1):
    jod += i 
print(f"The sum of first {a} natural number is ", jod)









#Take the input of a number and print its factorial

a = int(input("Please enter your number: "))
factorial = 1

for i in range(a,0,-1):
    factorial *= i 

print(f"factorial of {a} is ", factorial)










# Take an number and print even and odd numbers sum seperately

a = int(input("Enter your number: "))
odd = 0
even = 0 

for i in range(1,a+1):
    if i%2 == 0 :
        even += i
    else:
        odd +=i

print(f"Sum of even and odd numbers till {a} are {even}, {odd} respectively")










# Take an input and print all the factors of the number
a = int(input("Enter your number : "))

for i in range(1,a+1):
    if a%i==0:
        print(i)









# Accept a number and check it is perfect number or not

a = int(input("Enter your number: "))
sum = 0

for i in range(1,a):
    if a%i ==0:
        sum += i
if sum == a:
    print(f"Number {a} is an perfect number")
else:
    print(f"Number {a} is not a perfect number")










# check weather the number is prime or not 

a = int(input("Please Enter your number: "))
divisor_sum = 0

for i in range(1,a+1):
    if a%i ==0:
        divisor_sum += i

if divisor_sum == a + 1:
    print(f"Number {a} is a prime number")
else:
    print(f"Number {a} is not a prime number")









#Reverse a string

a = input("Enter any string sir!!! : ")
rev = ""
for i in range(len(a)-1,-1,-1):
     rev += a[i]
print(rev)








#check the function is palindrome or not
a = input("Enter your string sir!!! : ")
rev = ""
for i in range(len(a)-1,-1,-1):
    rev += a[i]
if rev == a:
    print(f"{a} is a palindrome")
else:
    print(f"{a} is not a palindrome")








#count the letter, digit and special symbol in this "str1 = "P@#yn26at^&i5ve"
str1 = "P@#yn26at^&i5ve"
alphabets=0
number=0
special_Char=0
for i in range(len(str1)):
    if str1[i] >= "a" and str1[i] <="z" or str1[i] >="A" and str1[i] <='Z':
        alphabets += 1
    elif str1[i] >= "0" and str1[i] <= "9":
        number += 1
    else:
        special_Char += 1
print(f"total alphabets are {alphabets}")
print(f"total numbers are {number}")
print(f"total numbers of special characters are {special_Char}")




