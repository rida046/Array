
from labprog9 import product_details


def test_product_details():
    result = product_details(101, "Laptop", 2, 45000)

    expected = (
        "Product ID: 101\n"
        "Product Name: Laptop\n"
        "Quantity: 2\n"
        "Price: Rs. 45000.00"
    )

    assert result == expected


def test_another_product():
    result = product_details(102, "Mouse", 5, 500)

    assert "Product Name: Mouse" in result
    assert "Quantity: 5" in result
