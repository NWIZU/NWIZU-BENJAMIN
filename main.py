name=input("enter your name:")
birth_year=int(input("enter your birth year:"))
birth_month = int(input("enter your birth month(1-12)"))
for month in birth_month:

    if month>12:
     print("error: enter a valid month")
    elif month<12:
        continue
    else:
        break





birth_day=int(input("enter your birth day(1-31):"))

current=2025
age=current-birth_year
print(f"{name},your age is {age}.")



