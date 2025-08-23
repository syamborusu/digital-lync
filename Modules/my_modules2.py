# This is my custom user defined module
name = "Edify"
email = "edify@gmail.com"

def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def profile_info(name=name,email=email): # dynamic
    return f"Hi {name} you logged in with email {email}"