# If Statement
discount = int(input("Enter discount rate: "))
amount = int(input("Enter discount amount: "))

# Check he amount value
if amount > 1000:
   discount = amount * 10 / 100

print("amount = ", amount - discount)