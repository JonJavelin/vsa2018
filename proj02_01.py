# Name:
# Date:

# proj02: sum
#initialize loop control variable
loop_control = 0
counter = 0
#start loop
while loop_control < 100 and counter >0:
    print "I have" + str(loop_control) + "oofs"
if loop_control /2 == 0:
    print  "This is even"
else:
    print "This is odd"
    #update loop control variable
    loop_control = loop_control + 3
# Write a program that prompts the user to enter numbers, one per line,
# ending with a line containing 0, and keep a running sum of the numbers.
# Only print out the sum after all the numbers are entered
# (at least in your final version). Each time you read in a number,
# you can immediately use it for your sum,
# and then be done with the number just entered.

#Example:
# Enter a number to sum, or 0 to indicate you are finished: 4
# Enter a number to sum, or 0 to indicate you are finished: 5
# Enter a number to sum, or 0 to indicate you are finished: 2
# Enter a number to sum, or 0 to indicate you are finished: 10
# Enter a number to sum, or 0 to indicate you are finished: 0
#The sum of your numbers is: 21
sum = 0
input = 1
#start loop
while  input != 0:
    input = int(raw_input("Enter a number to add to the sum, or enter 0 to indicate that you are done"))
    sum = sum + input
print "Your sum is " + str(sum) + "!"
