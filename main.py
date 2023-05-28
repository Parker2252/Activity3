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


def get_letterGrade(averageEarned):
    if averageEarned >= 92:
        return "A"
    elif averageEarned >= 88:
        return "B+"
    elif averageEarned >= 82:
        return "B"
    elif averageEarned >= 78:
        return "C+"
    elif averageEarned >= 70:
        return "C"
    elif averageEarned >= 60:
        return "D"
    else:
        return "F"


def main():
    display_title()



if __name__ == "__main__":
    main()
