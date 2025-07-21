#types of printing in python
# 1. Using print function
print("helloworld")
# 2. Using f-string (formatted string literals)
name = "Syam"
print(f"Hello, {name}!")
# 3. Using format method
age = 25
print("Hello, {}! You are {} years old.".format(name, age))
# 4. Using % operator (old-style formatting)
print("Hello, %s! You are %d years old." % (name, age))
# 5. Using join method
greeting = "Hello"
parts = [greeting, name]
print(" ".join(parts) + "! You are " + str(age) + " years old.")
#7.using End parameter