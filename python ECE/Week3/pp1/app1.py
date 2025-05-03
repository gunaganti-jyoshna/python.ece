#3.Defining and Using Functions
#a)Write a function to read data from a file and display it on the screen
import os

filename = input("Enter the name of the file with .txt extension: ")

if os.path.exists(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line, end='')
else:
    print("The file was not found. Please check the name and try again.")

