from typing import Any



### Challenge Questions
### Get a List




def get_list():
    values_list: list[Any] = []
    while True:
        value = input("Enter a value: ")
        if value.strip() != "":
            values_list.append(value)
        else:
            print(f"Here's the list: {values_list}")
            break 

if __name__ == "__main__":
    get_list()
            
            






