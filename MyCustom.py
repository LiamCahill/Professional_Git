#! /usr/bin/env

import subprocess
import csv



def main():
    x = 5
    print(x)
    printType(x)

# My own function to print variable types
def printType(value):
    print(type(value))

def myName(enterName):

    #name = input("What is your name? ")
    print("Hello " + enterName + ".")

def terminalCommand():
    subprocess.call("ssh liamcahill@10.0.0.129", shell=True)

def csvStats(thisFile):
    fields = []
    rows = []

    with open(thisFile, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)

        print("Total number of rows: %d"%(csvreader.line_num))

        print('Field names are:' + ' , '.join(field for field in fields))

        #print first 5 rows
        print('\nFirst 5 rows are: \n')
        for row in rows[:5]:
            for col in row:
                print("%10s"%col),
            print('\n')



if __name__ == "__main__":
    #enterName = input("Please enter your name.")
    #myName(enterName)

    thisFile = input("What file do you want to edit?")
    csvStats(thisFile)

    #proof of concept for Maura
    #print(len("Hel" + "lo!"))