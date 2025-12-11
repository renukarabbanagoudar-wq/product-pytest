def get_product_info(product_id, name, quantity, price):
    """
    Returns a well-formatted string with product details.
    """
    return (
        f"Product Information:\n"
        f"ID: {product_id}\n"
        f"Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: ₹{price:.2f}"
    )
if __name__ == "__main__":
    print(get_product_info(101, "Laptop", 5, 55000.50))