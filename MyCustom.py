#! /usr/bin/env

import subprocess



def main():
    x = 5
    print(x)
    printType(x)

# My own function to print variable types
def printType(value):
    print(type(value))

def myName():
    name = input("What is your name? ")
    print("Hello " + name + ".")

def terminalCommand():
    subprocess.call("ssh liamcahill@10.0.0.129", shell=True)

if __name__ == "__main__":
    terminalCommand()

# This will also execute, regardless if this script is imported somewhere.
# That's why we need a main() function.
print('Welcome to the Python')
