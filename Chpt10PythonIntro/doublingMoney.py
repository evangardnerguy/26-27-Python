# =================================================================
# Script Name: doublingMoney.py
# Lesson: Algorithm Design 10.9

# Problem: You put $10,000 into an account that earns 5% interest per year, how many years until the balance doubles?

# Pseudocode
#   Set year to 0, balance to 10,000
#   While balance is less than 20,000
#       Add 1 to the year.
#       Set interest rate to balance x 0.05.
#       Add interest to the balance
# Report year as the answer.
# ============================================

year = 0
balance = 10000

while balance < 20000:
    year += 1
    interest = balance * 0.05
    balance = balance + interest
print("Years to double:", year)
print("Final Balance:", f"{balance:.2f}")