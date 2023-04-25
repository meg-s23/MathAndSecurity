"""This program provides the user with a menu to generate a password, calculate
and format a percentage, displays how many days until 7/4/25, use the law of
cosines to calculate the leg of a triangle, calculate the volume of a right
circular cylinder, exit program option"""
#Developer: Megan Moore
#SDEV300/6380 Lab2
#Jan 24, 2023
#Imports for program
import sys
import secrets
from datetime import date
import string
import math as mt
#Function to display errors in red
def print_error(*args, **kwargs):
    """Displays error message in red if input incorrect"""
    print(*args, file=sys.stderr, **kwargs)
#Password function
def password():
    """Function takes user input to create secure password"""
#Variables for password function
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
#Concatenate the string to create password
    alphabet = letters + digits + special_chars
#Ask user for how long of password needed
    pwd_length=int(input('How long of password is needed? '))
    pwd = ''
#For statement to generate and print password
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    print('Password Generated:\n' ,pwd)
#Program restarts
    print('\n**Main Menu**\n')
#Percentage function
def percentage():
    """Function takes input to calculate and format a percentage"""
#Ask user for the numerator
    num=float(input('What is the numerator?'))
#Ask user for the denominator
    denom=float(input('What is the denominator?'))
#Create percentage equation
    percent=(num/denom * 100)
#Format percentage
    print(f'{percent:.2f}')
#Program restarts
    print('\n**Main Menu**\n')
#Calendar function
def calendar():
    """Function calculates amount of days until July 4, 2025"""
#Variables for calendar date calculation
    now = date.today()
    future= date(2025, 7, 4)
    delta=future-now
#Display today's date and number of days between July 4, 2025
    print('Today date is: ', now)
    print(f'The number of days between {now} and July 4, 2025 is: ')
    print(delta.days)
#Program Restarts
    print('\n**Main Menu**\n')
#Triangle Function
def triangle():
    """Function uses law of cosines to calculate leg of triangle"""
#Ask user for known angle and length
    c=float(input('What is the angle of C ?'))
    a=float(input('What is the length of A ?'))
    b=float(input('What is the length of B ? '))
#Calculate input using cosine rule
    answer=mt.sqrt((a * a) + (b * b) - 2.0 * a * b * mt.cos(c/180.0*mt.pi))
#Format answer to display 2 decimal places
    print('The length of C is: ')
    print(f'{answer:.2f}')
#Program Restarts
    print('\n**Main Menu**\n')
#Cylinder Function
def cylinder():
    """Function calculates volume of right circular cylinder"""
#Ask user for radius
    radius=float(input('Enter the radius of the cylinder'))
#Ask user for height
    height=float(input('Enter the height of the cylinder'))
#Calculate the volume of cylinder
    volume=mt.pi*pow(radius,2)*height
#Display volume of cylinder
    print('The volume of the cylinder will be:')
    print(f'{volume:.2f}')
#Program Restarts
    print('\n**Main Menu**\n')
#Main Menu Function
def menu():
    """Function displays menu options, option calls function"""
    print('*' * 50)
    print('Welcome to the Python Math and Security Program')
    while True:
        print('1: Generate Secure Password\n'
            '2: Calculate and Format a Percentage\n'
            '3: Number of Days Until July 4, 2025\n'
            '4: Calculate Triangle Using Law of Cosines\n'
            '5: Calculate Volume of Right Circular Cylinder\n'
            '6: Exit program\n')
        try:
            choice=int(input('Enter selection: '))
            if choice == 1:
                print('**Menu option (1) selected**')
                password()
            elif choice == 2:
                print('**Menu option (2) selected**')
                percentage()
            elif choice == 3:
                print('**Menu option (3) selected**')
                calendar()
            elif choice == 4:
                print('**Menu option (4) selected**')
                triangle()
            elif choice == 5:
                print('**Menu option (5) selected**')
                cylinder()
            elif choice == 6:
                sys.exit('Thank you for using the program. Goodbye')
        except ValueError:
            print_error('***Input must be an Integer***')
menu()
def main():
    """calls funtions for program to run"""
    menu()

if __name__ == "__main__":
    main()
