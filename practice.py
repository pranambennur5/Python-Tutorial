'''
#Practice #1 Enter Username and Password

while True:
    name = input('Enter your Username:')
    if name != 'Pranam':
        print('(Please enter the correct Username)')
        continue
    password = input('Hello Pranam, please enter your password:')
    if password == 'Starfish':
         break
print('Thank you')

name = input('Enter a name:')
for i in range(5):
    print(name,'(',i,')')


#Practice 2

name = input('Enter number 1 or 2: ')
if name == str(1) :
    print('Hello')
elif name == str(2):
    print('Howdy')
else:
    print('Greetings')


#Practice 3

for i in range(1,11):
    print('For loop:', i)
    
anum = 0
while num < 10:
    num = num+1
    print('While loop:', num)


#Practice 4

catNames = []

while True: 
    print('Enter the name of Cat ', str(len(catNames) + 1), 'Or enter nothing to stop.')
    name = input()
    catNames = catNames + [name]
    if name == "":
        print("The cat names are: ")
        for i in catNames:
            print(" ", i)
        break


#Practice 5, Enter your name and age.

print("Enter you name: ")
myName = input()
print('Hello ' +myName+ ', Google welcomes you')
print("Below is the length of your name")
print(len(myName))
print("What is your age??")
myAge = input()
print('After 5 years you will be ' +str(int(myAge)+5)+ ' years old.' )

#Practice 6, Check continue and break

while True:
    print("Enter your name ")
    name = input()
    if name != "Pranam":
        continue
    print("Hello " +name+ ", Please enter your password")
    password = input()
    if password == "Bennur":
        break
print("Welcome and Thanks")
'''

