def show_discount_details(price: float, discount: float) -> None:
    """
    Calculate and display discount details.
    """
    discount_amount = price * discount / 100
    final_price = price - discount_amount

    print(f"Original price: {price}")
    print(f"Discount: {discount}%")
    print(f"Final price: {final_price}")


price = 1000
discount = 20

show_discount_details(price, discount)