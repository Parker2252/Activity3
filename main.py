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






if __name__ == "__main__":
    display_title()
    get_totalPoints()