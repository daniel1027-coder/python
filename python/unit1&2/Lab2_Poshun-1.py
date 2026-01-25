"""
Restaurant Tip Calculator
Poshun Lin

To calculate total bill with the suggested percentage of tip to customers
No starter code was used. This program was written from scratch

01/25/2026
"""

dinner_cost = float(input("enter the cost: $"))

tip15 = dinner_cost * 0.15
tip20 = dinner_cost * 0.2 

total_15 = dinner_cost + tip15
total_20 = dinner_cost + tip20

print(f"Suggested 15% tip will be: ${tip15:.2f}")
print(f"Suggested 20% tip will be: ${tip20:.2f}")
print(f"Total bill with 15% tip will be: ${total_15:.2f}")
print(f"Total bill with 20% tip will be: ${total_20:.2f}")