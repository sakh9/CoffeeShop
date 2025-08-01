import pytest
from CoffeeShop import Customer, Coffee, Tea, Food, Order

def test_customer_creation():
    c = Customer("Alby")
    assert c.get_name() == "Alby"

def test_tea_customization():
    tea = Tea("Jasmine", 15000)
    tea.set_customization("Short", "More")
    assert tea.cup_size == "Short"
    assert tea.ice_level == "More"

def test_add_item_to_order():
    order = Order()
    coffee = Coffee("Americano", 24000)
    order.add_item(coffee, 2)
    assert len(order.cart) == 1
    assert order.cart[0][1] == 2  # quantity

def test_update_item_in_order():
    order = Order()
    food = Food("Croissant", 15000)
    order.add_item(food, 1)
    order.update_item(0, 3)
    assert order.cart[0][1] == 3

def test_clear_order():
    order = Order()
    tea = Tea("Java Tea", 15000)
    order.add_item(tea, 1)
    order.clear_order()
    assert len(order.cart) == 0
