
# print all integers from 0 to 150
for i in range(0, 151):
    print(i)

# Print all the multiples of 5 from 5 to 1,000
for i in range(5, 1000):
    if(i % 5 == 0):
        print(i)

# Print integers 1 to 100. if divisible by 5, print "Coding". instead if divisible by 10 print Coding with me.
for i in range(1, 101):
    if(i % 10 == 0):
        print("Coding")
    elif i % 5 == 0:
        print("Coding with me")
    else:
        print(i)

# Add odd integers from 0 to 500,000 and print the final sum.
sum = 0
for i in range(1, 5000001, 2):
    if(i % 2 !=0):
        sum += i
print(sum)

# Print positive numbers starting at 2018 counting down by four
for i in range(2018, 0, -4):
    if i % 2 == 0:
        print(i)

"""
Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9
"""
low_num = 2
high_num = 9
mult = 3

for i in range(low_num, high_num +1): #we use +1, to generate a sequence including 9 which is the upper limit of of the range. if we dont use +1 like low_num, high_num it would generate a sequence which 9 in not included like[2,3,4,5,6,7,8].
    if i % mult == 0:
        print(i)

