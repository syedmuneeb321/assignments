import math
# Age Assignments Based on the Riddle

Anton: int  = 21
Beth: int  = 6
Chen: int  = 20
Drew: int  = Chen + Anton 
Ethan: int  = Chen 

print("Anton: " + str(Anton))
print("Beth: " + str(Beth))
print("Chen: " + str(Chen))
print("Drew: " + str(Drew))
print("Ethan: " + str(Ethan))
print("\n")

## ============================================================================= ## 

# Formatted String Interpolation

name:str = "Alice"
age:int = 30
city:str = "New York"
print(f"{name} is {age} years old and lives in {city}.")

## ============================================================================= ##

# String Manipulation
s:str = "hElLo WoRlD"
print(s.capitalize())
print(s.upper())
print(s.lower())
print("\n")
## ============================================================================= ##

# Substring Search

s:str ="the quick brown fox jumps over the lazy dog" 
print(f"index of fox {s.index("fox")}")

print(f"'the' appears {s.count("the")} times")
print("\n")
## ============================================================================= ##
# String Replacement
s:str ="I love programming in Python"
print(s.replace("Python","Java"))
print("\n")

## ============================================================================= ##
# String Splitting and Joining
fruits:str ="apple,banana,cherry,dates"
fruits_list: list[str] = fruits.split(",")
print(fruits_list)
print(" ".join(fruits_list))
print("-".join(fruits_list))
print("\n")

## ============================================================================= ##
# String Stripping and Justifying
s:str ="   Python is fun!   "
sentence: str = s.strip()
print(sentence)
left_justify = sentence.ljust(20, "*")
right_justify = sentence.rjust(20,"*")
print(left_justify)
print(right_justify)
print("\n")
## ============================================================================= ##
# Convert an integer to its binary representation
num:int = 45 
binary_num = bin(num)
print("Binary representation :",binary_num)
print("\n")

## ============================================================================= ##
# Calculate Powers of Numbers.
base:int = 3
exponent:int = 4
# print("power result:",base**exponent)
print("power result:",round(math.pow(base,exponent)))
print("\n")

## ============================================================================= ## 
# Round floating-point numbers
value:float = 12.34567

print(f"Rounded to nearest integer: {round(value)}")
print(f"Rounded to nearest integer: {round(value,2)}")









