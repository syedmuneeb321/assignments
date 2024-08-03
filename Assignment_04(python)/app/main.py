import math
# from app.get_list import get_list
# from app.get_last_element import get_last_element
from get_list import get_list
from get_last_element import get_last_element
def main() -> None:
    # Add two numbers
    num1: int = int(input("Enter a first number:"))
    num2: int = int(input("Enter a second number:"))
    total: int = num1 + num2
    print(f"Sum of {num1} and {num2} is {total}")
    print("\n")

    ## ============================================================================= ## 

    # Agreement Boot

    animal_name: str = input("Enter a Favourite Animal name:")
    print(f"My favourite animal is also {animal_name}")
    print("\n")

    ## ============================================================================= ##

    # Fahrenheit to Celsius
    fahrenheit_temp: float = float(input("Enter temperature in Fahrenheit:"))
    degrees_celsius: float = (fahrenheit_temp-32)*5.0/9.0
    print(f"Temperature: {fahrenheit_temp}F={degrees_celsius}C")
    print("\n")

    ## ============================================================================= ##

    # Triangle Perimeters
    side1: float = float(input("Enter first side:"))
    side2: float = float(input("Enter second side:"))
    side3: float = float(input("Enter third side:"))
    perimeter: float = side1+side2+side3
    print(f"Perimeter of triangle is {perimeter}")
    print("\n")

    

    ## ============================================================================= ##
    # Square Number
    number: float = float(input("Type a number to see its square:"))
    square_root:float = number ** 2 
    print(f"Square of {number} is {square_root}")
    print("\n")

    ## ============================================================================= ##

    # Delete a number in list 
    numbers: list[int] = [1, 2, 3, 4, 5]
    print(numbers)
    # del numbers[2] 
    numbers.remove(3)
    print(numbers)
    print("\n")

    ## ============================================================================= ##

    # Creating a list 
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [4, 5, 6]
    # print(list1+list2)
    list1.extend(list2)
    print(list1)
    print("\n")
    ## ============================================================================= ##

    # Pop Method 
    items: list[int] = [10, 20, 30, 40]
    print(items)
    items.pop()
    print(items)
    print("\n")
    ## ============================================================================= ##
    # Index Method 
    colors: list[str] = ["red","blue","green","yellow"]
    print(f" green color index is {colors.index("green")}")
    print("\n")

    ## ============================================================================= ##














if __name__ == "__main__":
    main()
    get_list()
    get_last_element(["ali","ahmad","zohaib"])


