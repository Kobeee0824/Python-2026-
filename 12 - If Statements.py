is_male = True
is_tall = False

if is_male or is_tall:#kahit isa sa kanila is true
    print("You are a male or tall or both")
else: 
    print("You neither male nor tall")

print("--------------------------")

is_male = True
is_tall = False

if is_male and is_tall:#dapat both ay true
    print("You are a tall male")
else: 
    print("You either not male or not tall or both")

print("--------------------------")

is_male = False
is_tall = True

if is_male and is_tall:#dapat both ay true
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall") 
else: 
    print("You either not male and not tall")


dog = "Tasha"

if dog == "Tasha":
    print("Good Dog!")
else:
    print("Bisting Dog")


