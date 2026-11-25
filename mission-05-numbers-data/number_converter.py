def main():
    try:
        user_input = input("Enter a positive decimal number: ")
        decimal_val = int(user_input)
        if decimal_val < 0:
            print("Please enter a positive number.")
            return

        binary_val = bin(decimal_val)
        hex_val = hex(decimal_val)

        print(f"Decimal: {decimal_val}")
        print(f"Binary: {binary_val}")
        print(f"Hexadecimal: {hex_val}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
