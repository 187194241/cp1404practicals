"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

def main():
    score = float(input("Enter score: "))
    print(assess_score(score))
    ran_score = random.randint(0,100)
    print(assess_score(ran_score))

def assess_score(score):
    while score < 0 or score > 100:
        return "Invalid score"
        score = float(input("Enter score: "))
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    else:
        return "Excellent"


main()