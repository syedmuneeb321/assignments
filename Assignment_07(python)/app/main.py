
import math

def is_prime(n:int)->bool:
    if n <= 1:
        return False
    
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    


def main()->None:
    favourite_number_list: list[int] = []
    user_name: str = input("Enter your name:")
    for i in range(0,3):
        fav_num = int(input(f"Enter your {i+1} favorite number:"))
        favourite_number_list.append(fav_num)
    print(" ")
    print(f"Hello, {user_name}! Let's explore your favorite numbers:")
    tuple_number_list: list[tuple[int,int]] = []
    for j in favourite_number_list:
        if j % 2 == 0:
            print(f"The number {j} is even")
            tuple_number_list.append((j,pow(j,2)))

        else:
            print(f"The number {j} is odd")
            tuple_number_list.append((j,pow(j,2)))


    for tuple_number in tuple_number_list:
        print(f"The number {tuple_number[0]} and its square: {tuple_number}")

    sum_of_fav_num: int = sum(favourite_number_list)
    print(f"Amazing! The sum of your favorite numbers is: {sum_of_fav_num}")
    if is_prime(sum_of_fav_num):
        print(f"Wow, {sum_of_fav_num} is a prime number!")
    # else:
    #     print(f"Wow, {sum_of_fav_num} is a even number!")








if __name__ == "__main__":
    main()