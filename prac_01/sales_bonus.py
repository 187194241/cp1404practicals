"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
LOW_THRESHOLE = 0.1
HIGH_THRESHOLE = 0.15
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * LOW_THRESHOLE
    else:
        bonus = sales * HIGH_THRESHOLE
    print(f"Your bonus is ${bonus:.2f}")
    sales = float(input("Enter sales: $"))
