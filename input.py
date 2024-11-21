# Eduardo Imbronizio Zatti
# Making a change to test updating repo on github

name = input("What is your name?")
print(name)

try:
    num = int(input("Enter a number: "))
    print(num)
except:
    print("You did not enter a number.")
    
answer=42
print("The answer is",answer) # when you use the comma it automatically adds the space

for i in range(5):
    print(i, end=" ")
print()

age=14
name="Jim"
print(f"{name}, in {18-age} years you can vote.")

'''reading a file line by line'''
with open('movies.txt') as file:
    for line in file:
        line = line.strip()
        #print(line)
        
'''reading a file line by line'''
with open('heights.txt') as file:
    for line in file:
        line = line.strip()
        #print(line)
        ''' Splits the information in the line and stores them in a list'''
        #info = line.split()
        '''Stores the values in three variables'''
        fname, lname, height = line.split()
        print(fname, lname, height)