# 2. Write a program that checks if a given string is palindrome.
string=input("Enter String")
rev=""
for char in string:
    rev=char+rev
if rev==string:
    print("Pallindrome")
else:
        print("not Pallindrome")