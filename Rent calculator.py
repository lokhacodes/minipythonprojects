# Rent and Expense Splitter

# Collecting inputs
rent = float(input("Enter total monthly rent for the flat: "))
food_cost = float(input("Enter total shared food/snack expenses: "))
units_used = float(input("Enter electricity units consumed: "))
rate_per_unit = float(input("Enter cost per electricity unit: "))
num_people = int(input("Number of roommates sharing the flat: "))

# Calculating electricity and total expenses
electricity_bill = units_used * rate_per_unit
total_expense = rent + food_cost + electricity_bill

# Cost per person
individual_share = total_expense / num_people

# Output
print(f"\n🔹 Total amount to be split: {total_expense:.2f}")
print(f"💰 Each person needs to pay: {individual_share:.2f}")
