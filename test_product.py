from product import get_product_info

def test_get_product_info():
    product_id = 101
    name = "Laptop"
    quantity = 5
    price = 55000.50

    expected_output = (
        "Product Information:\n"
        "ID: 101\n"
        "Name: Laptop\n"
        "Quantity: 5\n"
        "Price: 55000.50"
    )

    assert get_product_info(product_id, name, quantity, price) == expected_output
