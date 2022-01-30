'''
#First Execution:
print("\n");
print("Hello Pranam, you are going to be a Master in Python Programming", "\n");

#Print 1 to 10 using Python

for i in range(0,11):
        print(i);

print("\n");

n=0;
while(n<=10):
        print(n);
        n=n+1;

#An exmaple for a function

print("\n")

def triangleArea(base, height):
    return base*height/2

area_1 = triangleArea(3,4)
area_2 = triangleArea(5,8)
sum = area_1 + area_2
print(sum)
print("\n")

#Arguments with the key. Order doesn't matter

def family(name1, name2, name3, name4):
        print("My family members are: " +name1+ "," +name2+ "," +name3+ "," +name4+ ".")

family(name2 = "Bharathi", name3 = "Pranam", name1 = "Rajashekar", name4 = "Prerana")
print("\n")

#Passing a list as an Argument

def favSongs(songs):
        for i in songs:
                print(i)

favorites = ["Till I Collapse", "Not Afraid"]
favSongs(favorites)
print("\n")


#Factorial using For Loop

def factorial(x):
    if x<0:
        return -1
    else:
        
        fact = 1
        for i in range(1,x+1):
            fact = fact * i
    return fact

result = factorial(5)
print(result)
print("\n")

#Factorial using recursive function
def factorial(x):
    if x<0:
        return -1
    elif x<2:
        return 1
    else:
        y = x * factorial(x-1)
        return y

result = factorial(5)
print(result)
print("\n")


#Login using correct username and password

while(True):
    username = input("Hello, Please enter your username: ")
    if username != "Pranam":
        print("Hello, please enter your correct username")
        continue
    else:
        password = input("Please enter your password ")
        if password == "password":
            print("Your login is successfull")
            break
        else:
            print("Login Failed")
            continue
print("\n")


#Converting Celsius to Fahrenhite

def degtofah(n):
    return ((celsius * 9/5) + 32)

celsius = 32
print(celsius,"C", degtofah(celsius),"F")
print("\n")

#Count how many digits the number has

def digitCount(n):
    count = 0
    if n == 0:
        return 1
    while(n>=1):
        count +=1
        n = n/10
    return count

print(digitCount(88988))
print("\n")


#The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise.

def counter(start, stop):
    count = start
    if start > stop:
        return_count = "Counting Down "
        while(count>stop):
            return_count +=str(count) + ","
            count -= 1
    else:
        return_count = "Counting Up "
        while(count<stop):
            return_count += str(count) + ","
            count += 1
    return_count += str(stop)
    return return_count     
    

print(counter(1,10))
print(counter(2,1))
print(counter(5,5))
print("\n")


#Check whether a number is even or odd

def isEven(n):
    if n%2 == 0:
        return True
    else:
        return False

print(isEven(0))
print("\n")


#Print a character using indexing

name = ("Pranam")

for i in range(6):
    print(name[i], end="")
print("\n")
      
#Find an index of a character

message = "Hello, I am Pranam Bennur"
print(message.index("P"))
print("\n")



#Replace old domain in an email with new domain. 


def replaceDomain(email,old_domain,new_domain):
    if "@" + old_domain in email:
        index = email.index("@"+old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

print(replaceDomain("pranam@outlook.com", "outlook.com", "gmail.com"))
print(replaceDomain("prerana@gmailcom", "outlook.com", "gmail.com"))
print("\n")


#Return the initials of the words contained in the phrase received, in upper case. example: "Universal Serial Bus" should return "USB"

def initials(w):
    words = w.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result


print(initials("Universal Serial Bus"))
print(initials("Kolar Gold Fields"))
print("\n")


#Example for Format Method

name = "Pranam"
number = len(name) * 3

print("Hey {}, your lucky number is {}".format(name, number))


print("Your lucky number is {number}, {name}".format(name=name, number=len(name)*3))
print("\n")



#Palindrome

def is_palindrome(word):
    splitWord = word.split()
    new_string = ''.join(splitWord)
    reversed_string = ''.join(reversed(new_string))
    if reversed_string.lower() == new_string.lower():
        return True
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
print("\n")


#The replace_ending function replaces the old string in a sentence with the new string, but only if the sentence ends with the old string.
#If there is more than one occurrence of the old string in the sentence, only the one at the end is replaced, not all of them.
#For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc.
#The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made)

def replace_ending(sentence, old, new):
    new_string = ""
    i = len(old)
    if sentence.endswith(old):
        new_string = sentence[:-i]+new
        return new_string
    return sentence
        


print(replace_ending("abcabc", "abc", "xyz"))
print(replace_ending("It's raining cats and cats", "cats", "dogs"))
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))

#List

fruits= ["Apple", "Oranges", "Pineapple", "Papaya"]
fruits.append("Avacado")
fruits.insert(0, "Strawberry")

print(fruits)
print("\n")



#The skip_elements function returns a list containing every other element from an input list, starting with the first element.

#Method 1
def skip_elements(elements):
    n = len(elements)
    new_list = []
    for i in range(0,n,2):
        new_list.append(elements[i])
    return new_list                    


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
print("\n")

#Method 2

def skip_elements(element):

    new_list = []
    i=0

    for item in element:

        if i<= len(element):

            new_list.append(element[i])

        i += 2

    return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))



#Return every other element from the list, this time using the enumerate function to check if an element is on an even position or an odd position.


def skip_elements(elements):
    result = []
    for index, element in enumerate(elements):
        if index%2==0:
            result.append(element)

    return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) 
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))



#Comprehension

#The odd_numbers function returns a list of odd numbers between 1 and n, inclusively.

def odd_numbers(n):
    return [x for x in range(1,n+1) if x%2==1]


print(odd_numbers(5))  
print(odd_numbers(10)) 
print(odd_numbers(11))




#Given a list of filenames, we want to rename all the files with extension hpp to the extension h

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

new_filename = []

for i in filenames:
    x = i.replace(".hpp",".h")
    new_filename.append(x)

print(new_filename)



def pig_latin(s):

    new_list = []
    split_list = s.split()
    for i in split_list:
        length = len(i)
        word = i[1:length] + i[-length] + "ay"
        new_list.append(word)
        

    return ' '.join(new_list)
    
print(pig_latin("programming in python is fun"))
print(pig_latin("hello how are you"))


#The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, …
#For example, group_list("g", ["a","b","c"]) returns "g: a, b, c".

def group_list(group, users):
    members = " ".join(users)
    return "{}: {}".format(group, members)


print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))

'''

name = input('Enter a name:')
for i in range(5):
    print(name,'(',i,')')
