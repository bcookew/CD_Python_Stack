num1 = 42 #variable declaration int
num2 = 2.3 #variable declaration float
boolean = True  #variable declaration bool
string = 'Hello World'  #variable declaration string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration dict
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration tuple
print(type(fruit)) #print result of a function call
print(pizza_toppings[1]) #print value at index 1 in list pizza_toppings
pizza_toppings.append('Mushrooms') #push mushrooms to the end of list pizza toppings
print(person['name']) #print value at key name in dict person
person['name'] = 'George' #set value at key name in dict person to george
person['eye_color'] = 'blue' #set value at key eye_color in dict person to blue
print(fruit[2]) #print value at index 2 in tuple fruit

if num1 > 45: #conditional if checking if variable num 1 greater than 45
    print("It's greater") #print string
else: #else conditional
    print("It's lower") #print string

if len(string) < 5: #if length of string less than 5
    print("It's a short word!") #print strint
elif len(string) > 15: #else if conditional
    print("It's a long word!") #print string
else: #conditional else
    print("Just right!") #print string

for x in range(5): #start a for loop
    print(x) # log statement
for x in range(2,5): #start a for loop in a specific range
    print(x) #log statement
for x in range(2,10,3): #start a for loop in a specific range
    print(x) # log statement
x = 0 #variable declaration
while(x < 5): #while loop start
    print(x) #log statement
    x += 1 #add to variable x

pizza_toppings.pop() #delete last value in list
pizza_toppings.pop(1) #delete value at index 1

print(person) #log statement variable
person.pop('eye_color') #delete value at key eye_color from dict person
print(person) #log statement

for topping in pizza_toppings: #loop through values in list pizza_toppings
    if topping == 'Pepperoni': #conditional checking lax equality
        continue #start new loop
    print('After 1st if statement')#log statement
    if topping == 'Olives':#conditional checking lax equality
        break #stop loop

def print_hello_ten_times(): #define a function 
    for num in range(10):#loop numbers in a range
        print('Hello') #log statement

print_hello_ten_times() #function call

def print_hello_x_times(x): #function definition
    for num in range(x): #loop x number of times
        print('Hello') #log statement

print_hello_x_times(4) #function call

def print_hello_x_or_ten_times(x = 10): #define function with a default variable 
    for num in range(x): #for loop start
        print('Hello') #log statement

print_hello_x_or_ten_times() #function call
print_hello_x_or_ten_times(4) #function call


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)