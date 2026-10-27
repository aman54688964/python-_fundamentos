# logical operators: or. and. not
# bool: true or false
b1 = True
b2 = False
print(f"the type of variable b1 is {int(b1)} and {int(b1)} respectively") 
print(f"the type of variable b2 is {int(b2)}");
condition1 = True 
condition2 = True
condition3 = False
product = (condition1 and condition2)
if condition1 and condition2:
    print("all conditions are satisfied")

print("practice 2")
print(condition1 or condition2)
print(condition1 or condition3)

if condition1 or condition2 or condition3:
    print("one of the conditions is satisfied")

condition1 = not condition1
print(condition1)
condition2 = False
if not condition1 and condition2 or condition3:
    print("condition1 is false and condition2 is true")
    print("what is happening")

print("logical operator priority:", False and True or True or False)
print("logical operator priority:", False and True or False or False)
print("logical operator priority:", False and False or False or False)


