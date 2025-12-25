def get_float(promt):
    while True:
        try:
            return float(input(promt))
        except ValueError:
            print("Enter the valid number")
    
no_of_people=int(input("Enter the number of people"))
names=[]
    
for i in range(no_of_people):
    name=input(f"Enter the name of person{i+1} ")
    names.append(name)

total_bill=get_float("Enter the bill amount ")
bill=round(total_bill/no_of_people,2)

print("\n"+"*"*20)
print(f"Total bill:{total_bill}")

for name in names:
    print(f"The bill for {name} is {bill}")

print("\n"+"*"*20)



