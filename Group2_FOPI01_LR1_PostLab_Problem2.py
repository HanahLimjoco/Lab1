from msilib.schema import File
from pickle import TRUE

print ("Welcome to File Reader\n")

file_open = input("Enter a File Name: ")

with open(file_open + ".txt", 'r') as f:
    print("")
    print(f.read() + "\n")

    user_Ans = input("Enter a line number from 1-10: ")

while user_Ans != "0":
       line = open(file_open + ".txt", 'r').readlines()[int(user_Ans) - 1]
       print(line)

       user_Ans = input("Enter a line number from 1-10: ")