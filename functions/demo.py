#without function
a = 18
b = 20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print("="*50)
# define a function
a = 100
b = 200
def arithmetic():
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)   
# call a function -> 100,200
arithmetic()

a = 1000
b = 2000

# call a function -> 1000,2000
arithmetic()

# Functions with parameters
def arithmetic(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

# call a function -> 1000,2000
arithmetic(5000,1000)
arithmetic(100,500)
# arithmetic(100)

# Positional Arguments 
def login(username,password):
    if username == "syam" and password == "12345":
        print("Login Success")
    else:
        print("Login Failed")

login("syam","12345") # exact order
login("syam","123") # exact order
login("12345","syam") # order changed

# Default Arguments 
def emp_info(emp_name,emp_email,emp_loc="Hyderabad",address="India"):
    print(f"Hi {emp_name} your email is {emp_email} and location is {emp_loc} actually from {address}")

# emp_info("Ravi","ravi@gmail.com","Hyderabad")
emp_info("Krishna","krishna@gmail.com")
emp_info("user3","user3@gmail.com")
emp_info("user4","Bangalore","user3@gmail.com")
emp_info("user5","user5@gmail.com","Pune","USA")

# Keyword Arguments 
def emp_info(emp_name,emp_email,emp_loc,address="India"):
    print(f"Hi {emp_name} your email is {emp_email} and location is {emp_loc} actually from {address}")

emp_info(emp_name="user4",emp_loc="Bangalore",emp_email="user3@gmail.com")


# Arbitrary Positional Arguments
def add_all(*numbers):
    total = 0
    for i in numbers:
        total = total + i
    print(f"Total is: {total}")

add_all()
add_all(1)
add_all(1,2)
add_all(1,2,3,4,5,6,7,8,9)

# Arbitrary Keyword Arguments (**kwargs)     
def profile(**info):
    print(info)

profile()
profile(id="101")
profile(id="102",name="Ravi")
profile(id=102,name="Ravi",rating=4.5)

# transactions
def cred_trans(**trans):
    print(trans)
    total = 0
    for i in trans:
        total = total + trans[i]
    print(f"You have done {len(trans)} and total value of all transactions is {total}")
cred_trans(jan=1000, feb=2000, mar=3000)        

# Using Both *args and **kwargs
def cred_trans_new(*trans, **info):
    print(trans)
    print(info)
    total = 0
    for i in trans:
        total = total + i
    print(f"Hi {info['name']} you have done {total} amount of transactions ")

cred_trans_new(1000,3000,5000,name="Ravi",email="ravi@gmail.com")

def new_fun(name, **info):
    pass
    
# functions without return keyword
def add(a,b):
    a+b
print(add(10,20))

# functions with return keyword
def add(a,b):
    return a+b
print(add(10,20))

# when using return, give appropriate responses
def add(a,b):
    return "Hello there"
print(add(10,20))

def new_math(a,b):
    return a+b
    return a-b
    return a*b

print(new_math(100,200))

def math_new(a,b,opr):
    if opr == "+":
        return a+b
    elif opr == "-":
        return a-b
    elif opr == "*":
        return a*b
    elif opr == "/":
        return a/b
    else:
        return "Invalid Operator"
    print("Code is Unreachable") 

print(math_new(3,4,"+"))    
print(math_new(3,4,"*"))
print(math_new(3,4,"'"))   

# Local Scope for variables
def add():
    # local variables are bb and cc
    bb = 5
    cc = 6
    print(bb) # accessing inside function
    print(cc) # accessing inside function
add()

# print(bb) # accessing outside function


# parameters passed to functions are also local variables
def add(bb,cc): # local variables are bb and cc 
    print(bb)
    print(cc)
add(10,20)
# print(bb) # accessing outside function

# global variable
aa = 30
def add(bb,cc): # local variables are bb and cc 
    print(bb) # accessing local variable inside function
    print(cc) # accessing local variable inside function
    print(aa) # accessing global variable inside function
add(1,2)    
print(aa) # accessing global variable outside function

# global variable
aa = 30
def add(bb,cc,aa): # local variables are bb and cc 
    print(bb) # accessing local variable inside function
    print(cc) # accessing local variable inside function
    print(aa) # accessing local variable inside function
    print(globals()['aa']) # accessing global variable when name conflict
add(1,2,3)    
print(aa) # accessing global variable outside function

# Trying to change global variable
count = 0
def increment():
    # count += 1 # local variable 'count' referenced before assignment
    global count
    count += 1 
increment()    
print("Count: ",count)
    
# function composition
def add(a,b):
    return a+b    

def sub(c,d,e):
    return add(c,d) - e

print(sub(3,4,5))

# to check builtins in python use __builtins__
# print(dir(__builtins__))

# builtin
text = "python"
len_text = len(text)
print("Using Builtin",len_text)

# simulate len with our way
def user_def_ln(s):
    count = 0
    for char in s:
        count += 1
    return count

text = "python"
len_text = user_def_ln(text)
print("Using User Defined",len_text)

# Instead of How To Do --> What To Do 

# without lambda
def add(a,b):
    return a+b
print(add(3,4))

# with lambda -> lambda arguments: expression    
sum = lambda a,b: a+b
print(sum)
print(sum(5,10))

# IILE
print((lambda a,b: a+b) (100,200))
print((lambda a,b: a*b) (100,200))


# without map 
# input [1,2,3,4] --> output [1,4,9,16]
def square_list(numbers):
    squared_list = []
    for n in numbers:
        squared_list.append(n * n)
    return squared_list

print(square_list([1,2,3,4]))

# with map 
# input [1,2,3,4] --> output [1,4,9,16]
# one liner functions 
# map(function, iterable)
print(map(lambda n: n * n, [1,2,3,4]))

print(list(map(lambda n: n * n, [1,2,3,4])))

# without filter
# input [1,2,3,4,5,6,7,8,9,10] --> Output [2,4,6,8,10]
def even_list(numbers):
    even_nums = []
    for n in numbers:
        if n % 2 == 0:
            even_nums.append(n)
    return even_nums

print(even_list([1,2,3,4,5,6,7,8,9,10]))

# with filter 
# input [1,2,3,4,5,6,7,8,9,10] --> Output [2,4,6,8,10]
# one liner functions 
# filter(function, iterable)
print(filter(lambda n: n % 2 == 0, [1,2,3,4,5,6,7,8,9,10]))
print(list(filter(lambda n: n % 2 == 0, [1,2,3,4,5,6,7,8,9,10])))

# without reduce
# input [1,2,3,4] -- output (1*2*3*4 = 24)
def multiply_list(numbers):
    result = 1
    for i in numbers:
        result = result * i
    return result
    
print(multiply_list([1,2,3,4]))

# with reduce
# input [1,2,3,4] -- output (1*2*3*4 = 24)
from functools import reduce
print(reduce(lambda x,y: x*y, [1,2,3,4]))

