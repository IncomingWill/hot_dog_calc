# Title: Hot Dog Calculator Program
# Program created by William Schaeffer
# CPS 313
# P. 163, Exercise 8, Hot Dog Cookout Calculator Program
# 01.18.22

# This program will take input and display supply details for a HD cookout

# Imports for math.ceil() function
import math

# CONSTANTS

DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

# User input

guestCount = int(input('How many guests are you expecting at the cookout? '))
dogsPerPerson = int(input('How many whole hot dogs will you prepare for each guest? '))

    # How many guests will not have a bun?
guestNoBuns = int(input('How many guests will not have a bun due to allergies or dietary restrictions? '))

    # Number to subtract based on guests with no buns and how many hotdogs will be prepared for them
noBuns = guestNoBuns * dogsPerPerson

# Calculations -> Use math.ceil() function to round up for needed packages

totalDogs = guestCount * dogsPerPerson
totalDogPackages = (totalDogs // DOGS_PER_PACKAGE)
totalBuns = totalDogs - noBuns
totalBunPackages = (totalBuns // BUNS_PER_PACKAGE)
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

