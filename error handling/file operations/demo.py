file=open("file.txt","r")
print(type(file))
print(file)  #it will give the file object
 #with open ("filepath",mode)
 #mode:r-read,w-write,a-append,r+-read and write
 #READ MODE
with open("file.txt","r") as New_file:
    print(type(New_file))
    #print(New_file.read())        #read all the content of file
    #for character in New_file.read():
       # print(character)  #read character by character
    #print(New_file.readline())   #read line by line
    #print(New_file.readlines())   #read all the line and store in list
    for line in New_file.readlines():
        print(line.strip()) 

    #WRITE MODE
with open("new.txt","w") as new_file:
    new_file.write("This is my new file\n")
    new_file.write("I am writing in my new file\n")
    new_file.write("I am appending in my new file\n")

with open("new.txt","w") as new_file:
    new_file.writelines(["welcome to python course\n","welcome to frontend\n","welcome to DSA\n"])


    #APPEND MODE
with open("new.txt","a") as new_file:  
    new_file.writelines(["welcome to HYDERABAD\n","welcome to INDIA\n","welcome to WORLD\n"])


#DELETE A FILE
#OS MODULE
#import os
#os.remove("new.txt")  #it will delete the file permanently