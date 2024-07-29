from typing import Any
### Challenge Questions

## Get last element

def get_last_element(lst:list[Any])->None:
    if len(lst) != 0:
        print(f"Last element is {lst[-1]}")
    else:
        print("List is empty")



user_list: list[str] = ['ali','ahmad','zohaib']
empty_list: list = []

if __name__ == "__main__":
    get_last_element(user_list)
    get_last_element(empty_list)
