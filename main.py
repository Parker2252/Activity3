# File: main.py
# Description: Python grade assigment
# Author: Parker Gornick
# Date: 5/28/23

def display_title(): # Function that says "Welcome to the grade Calculator
    print("Welcome to the Grade Calculator")


def get_totalPoints(): # Function that will ask the user for the total score and makes sure that it is an integer and
    # is in the range of 0 -1000.
    while True:
        try:
            total_points = int(input("\nEnter the total score (0-1000): "))
            if total_points < 0 or total_points > 1000:
                print("You must enter an integer value >= 0 and <= 1000. Try Again")
            else:
                print(total_points)
                return total_points
        except ValueError:
            print("You must enter an integer value >= 0 and <= 1000. Try Again")


def get_letterGrade(average_earned): #Function that chcekcs to find what the grade will be starting with A and working down to F.
    if average_earned >= 92:
        return "A"
    elif average_earned >= 88:
        return "B+"
    elif average_earned >= 82:
        return "B"
    elif average_earned >= 78:
        return "C+"
    elif average_earned >= 70:
        return "C"
    elif average_earned >= 60:
        return "D"
    else:
        return "F"


def main(): # Function that uses all 3 previous functions.
    display_title()
    while True:
        total_points = get_totalPoints()
        lettergrade = get_letterGrade(total_points / 1000 * 100) # Gets the letter grade
        percent = (total_points / 10) # Gets the number so that it is out of 100 not 1000
        print(f"You earned an average of {percent:.1f}%. Letter grade earned: {lettergrade}")

        choice = input("\nWould you like to enter another score (y/n)?: ") #Asks if the user wants to enter in more data
        while choice.lower() not in ['y', 'n']: # If there choice is not a Y or a N will keep asking till it gets y or n
            choice = input("Invalid input. Must enter 'y' or 'n': ")
        if choice == 'n': #Breaks out of while true if user choice is n
            break
    print()
    print("Thank You")


if __name__ == "__main__":
    main()
