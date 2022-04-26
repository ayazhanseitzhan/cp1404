"""
CP1404/CP5632 - Practical
Program to determine score status
"""

def main():
 score = float(input("Enter score: "))
 print(mark(score))


def mark(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif 50 <= score < 90:
        return "Passable"
    elif 90 <= score <= 100:
        return "Excellent"
    else:
        return "Bad"


main()
