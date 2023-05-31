# File: main.py
# Description: Python grade assigment
# Author: Parker Gornick
# Date: 5/28/23

def display_title():
    print("Welcome to the Grade Calculator")


def get_totalPoints():
    while True:
        try:
            total_points = int(input("Enter the total score (0-1000): "))
            if total_points < 0 or total_points > 1000:
                print("You must enter an integer value >= 0 and <= 1000. Try Again")
            else:
                print(total_points)
                return total_points
        except ValueError:
            print("You must enter an integer value >= 0 and <= 1000. Try Again")


def get_letterGrade(average_earned):
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


def main():
    display_title()
    while True:
        total_points = get_totalPoints()
        lettergrade = get_letterGrade(total_points / 1000 * 100)
        percent = (total_points / 1000 * 100)
        print(f"You earned an average of {percent:.1f}%. Letter grade earned: {lettergrade}")

        choice = input("Would you like to enter another score (y/n)?: ")
        if choice == 'n':
            break
    print()
    print("Thank You")


if __name__ == "__main__":
    main()
