# coding=utf-8
# Name:
# Date:

"""
proj04

practice with lists

"""

#Part I
#Take a list, say for example this one:



import time
num_list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.
print"First Stage"
num_list = 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
Value = int(raw_input("Pick a value that you want all numbers to be under"))
for number in num_list:
    if number < Value:
        print number









#Part II
# Take two lists, say for example these two:
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
time.sleep(3)
print "Second Stage"
for numbers in b and c:
    if numbers in b == numbers in c:
        print numbers

#Part III
# Take a list, say for example this one:
d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
# and write a program that replaces all “a” with “*”.
time.sleep(3)
print "Third Stage"
letter=d
for letters in d:
    if letter=="a":
        a = "*"
    else:
        letter=letter








#Part IV
#Ask the user for a string, and print out whether this string is a palindrome or not.
time.sleep(3)
print "Fourth Stage"
word = str(raw_input("Give me a word and i will see if it's a palindrome"))
let = int(raw_input("How many letters are in your word?"))
word = word.lower()
empty_list = []
empty_list.append(word)
n = 0
m = -1
e = empty_list[n]
i = empty_list[m]
loop_end = 1
#start loop
while let > -1 and loop_end!=0:
    let = let - 2
    if e == i:
        n=n+1 and m==m-1
    elif e!=i:
        print "This is not palindrome."
        loop_end="0"
    elif let==1:
        print "This is a palindrome"
        loop_end=0
    elif let==0:
        print "This is a palindrome!"
        loop_end=0













