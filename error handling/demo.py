a=10
b=2
 #ZeroDivisionError: division by zero
try:
    result=(a/b)
    print(result)   #it not throw the error skip if it was error
except:
    print("Cannot divise by zero")# execute if the try block cause the error else not execute

    #Or we can write by passing name
#except ZeroDivisionError:
    #print("Cannot divise by zero")

#else is execute if there is no error occurs that means if except is not execute then else will execute
else:
    print("Division successful")

#runs always,no matter what execute or not
finally:
    print("it's always run")

