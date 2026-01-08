from validate_age import *
from get_name import *

age = int(input("Enter your age: "))
validate_age(age)

print("="*35)
print("Welcome to voting eligilibity check")
print("="*35)
print("\n")

user_name = get_name()
print(f"Hello {user_name}!\n")
