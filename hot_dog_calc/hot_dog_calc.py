# Title: Hot Dog Calculator Program
# Program created by William Schaeffer
# CPS 313
# P. 163, Exercise 8, Hot Dog Cookout Calculator Program
# 01.18.22

# This program will take input and display supply details for a Hot Dog Cookout

# Imports
import math                             # For math.ceil() function
import sys                              # For Command-Line Args

# CONSTANTS

DOGS_PER_PACKAGE = 10                   # Total hot dogs per package      
BUNS_PER_PACKAGE = 8                    # Total buns per package

# Variable Declaration

    # Variables for user input

guestCount = int(sys.argv[1])           # Number of guests to attend
dogsPerPerson = int(sys.argv[2])        # Number of hot dogs to server per guest
guestNoBuns = int(sys.argv[3])          # Number of guests who will not eat buns

    # Variables for calculation

noBuns = 0                              # Total number of buns omitted, guestNoBuns * dogsPerPerson
totalDogs = 0                           # Total hot dogs to be prepared, guestCount * dogsPerPerson
totalDogPackages = 0                    # Total Hot Dog Packages needed for purchase, (totalDogs / DOGS_PER_PACKAGE) round up whole package
totalBuns = 0                           # Total Buns needed, totalDogs - noBuns
totalBunPackages = 0                    # Total Bun Packages needed, (totalBuns / BUNS_PER_PACKAGE) round up whole package
leftoverDogs = 0                        # Total leftover hotdogs, totalDogs modulus DOGS_PER_PACKAGE
leftoverBuns = 0                        # Total leftover buns, (BUNS_PER_PACKAGE * totalBunPackages) modulus totalBuns

# User input -- commented out so command line arguments can be used instead

#guestCount = int(input('How many guests are you expecting at the cookout? '))
#dogsPerPerson = int(input('How many whole hot dogs will you prepare for each guest? '))

    # How many guests will not have a bun?

#guestNoBuns = int(input('How many guests will not have a bun due to allergies or dietary restrictions? '))

    # Number to subtract based on guests with no buns and how many hotdogs will be prepared for them

noBuns = guestNoBuns * dogsPerPerson

# Calculations -> Use math.ceil() function to round up for needed packages

totalDogs = guestCount * dogsPerPerson
totalDogPackages = math.ceil(totalDogs / DOGS_PER_PACKAGE)
totalBuns = totalDogs - noBuns
totalBunPackages = math.ceil(totalBuns / BUNS_PER_PACKAGE)
leftoverDogs = totalDogs % DOGS_PER_PACKAGE
leftoverBuns = (BUNS_PER_PACKAGE * totalBunPackages) % totalBuns

# Display all of the details for the Hot Dog cookout

print(f'Total Guests Expected: {guestCount}')
print(f'Hot Dogs to prepare per guest: {dogsPerPerson}')
print(f'Total Guests who will not have a bun: {guestNoBuns}')
print(f'Total Hot Dogs Needed: {totalDogs}')
print(f'Total Hot Dog Packages Needed: {totalDogPackages}')
print(f'Total Hot Dog Buns Needed: {totalBuns}')
print(f'Total Hot Dog Bun Packages Needed: {totalBunPackages}')
print(f'Total Leftover Hot Dogs: {leftoverDogs}')
print(f'Total Leftover Hot Dog Buns: {leftoverBuns}')

#Demonstration of command line arguments borrowed from geeksforgeeks.org

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
     
# Addition of numbers
Sum = 0
# Using argparse module
for i in range(1, n):
    Sum += int(sys.argv[i])
     
print("\n\nResult:", Sum)
