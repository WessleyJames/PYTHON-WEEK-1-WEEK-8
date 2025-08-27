 # file: week_three_assignment.py

def calculate_discount(price, discount_percent):
    """Return final price after applying discount if >= 20%, else return original price."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price


# Prompt user for inputs
try:
    original_price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percent)

    print(f"Final Price: {final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values.")

