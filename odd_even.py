def is_even(num):
    return num % 2 == 0

def get_num():
    return int(input("Enter a number: "))

def main():
    print("Odd or even number")
    num = get_num()
    if is_even(num):
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")

# Run the main function
main()
