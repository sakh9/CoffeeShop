from abc import ABC, abstractmethod
from datetime import datetime
import asyncio

# MenuItem Abstraction & Encapsulation
class MenuItem(ABC):
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    @abstractmethod
    def display_item(self):
        pass

# Class Customer
class Customer:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

# Coffee Inheritance dari MenuItem
class Coffee(MenuItem):
    def __init__(self, name, price, cup_size = "Medium", milk_type = "Regular", sweet_level = "Normal", ice_level = "Normal"):
        super().__init__(name, price)
        self.cup_size = cup_size
        self.milk_type = milk_type
        self.sweet_level = sweet_level
        self.ice_level = ice_level

    def set_customization(self, size, milk, sweet, ice):
        self.cup_size = size
        self.milk_type = milk
        self.sweet_level = sweet
        self.ice_level = ice

    def display_item(self):
        print(f"Coffee: {self._name} - Rp{self._price:.0f} | Size: {self.cup_size}, Milk: {self.milk_type}, sweet: {self.sweet_level}, Ice: {self.ice_level}")

# Food Inheritance dari MenuItem
class Food(MenuItem):
    def display_item(self):
        print(f"Food: {self._name} - Rp{self._price:.0f}")

# Tea Inheritance dari MenuItem
class Tea(MenuItem):
    def __init__(self, name, price, cup_size = "Medium", ice_level = "Normal"):
        super().__init__(name, price)
        self.cup_size = cup_size
        self.ice_level = ice_level

    def set_customization(self, size, ice):
        self.cup_size = size
        self.ice_level = ice

    def display_item(self):
        print(f"Tea: {self._name} - Rp{self._price:.0f} | Size: {self.cup_size}, Ice: {self.ice_level}")

# Sistem pada Menu                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
class Menu(ABC):
    def __init__(self):
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def display_menu(self):
        for idx, item in enumerate(self.items, 1):
            print(f"{idx}. {item.get_name()} - Rp{item.get_price():.2f}")

    def get_item(self, index: int):
        if 0 <= index < len(self.items):
            return self.items[index]
        else:
            return None

# List Menu
class CoffeeMenu(Menu):
    def __init__(self):
        super().__init__()
        self.add_item(Coffee("Americano", 24000))
        self.add_item(Coffee("Cappuccino", 24000))
        self.add_item(Coffee("Bumi Latte", 24000))
        self.add_item(Coffee("Malty Latte", 27000))
        self.add_item(Coffee("Tiramisu Latte", 27000))
        self.add_item(Coffee("Aren Latte", 29000))
        self.add_item(Coffee("Cafe Latte", 29000))
        self.add_item(Coffee("Pandan Latte", 29000))
        self.add_item(Coffee("Nutty Oat Latte", 39000))
        self.add_item(Coffee("Buttercream Latte", 39000))
class TeaMenu(Menu):
    def __init__(self):
        super().__init__()
        self.add_item(Tea("Java Tea", 15000))
        self.add_item(Tea("Lemon Tea", 15000))
        self.add_item(Tea("Jasmine Tea", 15000))
        self.add_item(Tea("Strawberry Citrus Tea", 20000))
        self.add_item(Tea("Apple Cherry Tea", 20000))
        self.add_item(Tea("Mangosteen Tea", 25000))
class FoodMenu(Menu):
    def __init__(self):
        super().__init__()
        self.add_item(Food("sweet Glaze Donut", 11000))
        self.add_item(Food("Chocolate Cashew Donut", 11000))
        self.add_item(Food("Butter Croissant", 15000))
        self.add_item(Food("Chocolate Layer Croissant", 15000))
        self.add_item(Food("Tuna Mayo Sandwich", 22000))
        self.add_item(Food("Chicken Teriyaki Sandwich", 22000))
        self.add_item(Food("Cheesecake", 18000))
        self.add_item(Food("Strawberry Cheesecake", 18000))

# Order method
class Order:
    def __init__(self):
        self.cart = []

    def add_item(self, item: MenuItem, qty: int):
        self.cart.append((item, qty))

    def update_item(self, index: int, new_qty: int):
        item, _ = self.cart[index]
        self.cart[index] = (item, new_qty)

    def clear_order(self):
        self.cart = []

    def display_order(self, show_index=False):
        print("\n--- Your Order ---")
        total = 0
        for idx, (item, qty) in enumerate(self.cart, 1):
            sub_total = item.get_price() * qty
            if show_index:
                print(f"{idx}. {item.get_name()} x{qty} = Rp{sub_total:.0f}")
            else:
                print(f"{item.get_name()} x{qty} = Rp{sub_total:.0f}")
            total += sub_total
        print(f"Total: Rp{total:.0f}")
        return total

# Payment method
class Payment:
    def __init__(self):
        self.methods = ["Debit", "Kredit", "Qris", "Paypal", "OVO", "Dana"]

    def choose_method(self):
        print("\nPilih metode pembayaran:")
        for i, method in enumerate(self.methods, 1):
            print(f"{i}. {method}")
        while True:
            try:
                pilihan = int(input("Masukkan nomor metode: "))
                if 1 <= pilihan <= len(self.methods):
                    return self.methods[pilihan - 1]
                else:
                    print("Pilihan tidak tersedia.")
            except ValueError:
                print("UNVALID. . .")

# Main App
class CoffeeShop:
    def __init__(self):
        self.customer = None
        self.coffee_menu = CoffeeMenu()
        self.tea_menu = TeaMenu()
        self.food_menu = FoodMenu()
        self.order = Order()
        self.payment = Payment()

    # Start tampilan Program
    def start(self):
        while True:
            nama = input("\nEnter your name: ").title()
            self.customer = Customer(nama)
            while True:
                print(f"\n=== Welcome to Re:Zero {self.customer.get_name()} ===")
                print("1. Coffee Menu")
                print("2. Tea Menu")
                print("3. Food Menu")
                print("4. Change picked quantity")
                print("5. Checkout & Payment")
                print("6. Exit")
                print(f"\n {self.order.display_order()}")
                choice = input("Choose actions: ")
                print()

                if choice == "1":
                    self.process_menu(self.coffee_menu)
                elif choice == "2":
                    self.process_menu(self.tea_menu)
                elif choice == "3":
                    self.process_menu(self.food_menu)
                elif choice == "4":
                    if not self.order.cart:
                        print("No item can be change. Please order first.")
                    else:
                        self.update_order()
                elif choice == "5":
                    if not self.order.cart:
                        print("No item to pay. Please order first.")
                    else:
                        self.checkout()
                        self.order.clear_order()
                        break
                elif choice == "6":
                    if not self.order.cart:
                        print("There's nothing in your cart, Bye  /(^U^)/ !")
                        break
                    else:
                        confirm = input("Are you sure to cancel your order and exit ? (y/n): ").lower()
                        if confirm == "y":
                            self.order.clear_order()
                            print("Order canceled :( ")
                            break
                        else:
                            print("Return to menu.")
                else:
                    print("Pilihan tidak valid.")

    # Proses user memilih item
    def process_menu(self, menu: Menu):
        menu.display_menu()
        try:
            idx = int(input("Select menu number: ")) - 1
            item = menu.get_item(idx)
            if item:

                # Input jumlah Coffee yg diinginkan 
                if isinstance(item, Coffee):
                    customized_item = Coffee(item.get_name(), item.get_price())
                    self.customize_coffee(customized_item)
                    qty = int(input(f"Jumlah {customized_item.get_name()} yang diinginkan: "))
                    if 1 <= qty <= 10:
                        self.order.add_item(customized_item, qty)
                        print(f"{qty} {customized_item.get_name()} ditambahkan ke pesanan.")
                    else:
                        print("Max 10 pcs.")

                # Input jumlah Tea yg diinginkan
                elif isinstance(item, Tea):
                    customized_item = Tea(item.get_name(), item.get_price())
                    self.customize_tea(customized_item)
                    qty = int(input(f"Jumlah {customized_item.get_name()} yang diinginkan: "))
                    if 1 <= qty <= 10:
                        self.order.add_item(customized_item, qty)
                        print(f"{qty} {customized_item.get_name()} ditambahkan ke pesanan.")
                    else:
                        print("Max 10 pcs.")

                # Anggap untuk Food, karena tdk ada instance
                else:
                    qty = int(input(f"Jumlah {item.get_name()} yang diinginkan: "))
                    if 1 <= qty <= 10:
                        self.order.add_item(item, qty)
                        print(f"{qty} {item.get_name()} ditambahkan ke pesanan.")
                    else:
                        print("Max 10 pcs.")

            else:
                print("Item tidak ditemukan.")
        except ValueError:
            print("UNVALID. . .")

    # Perubahan user pd item Coffee
    def customize_coffee(self, coffee_item: Coffee):
        # Americano Tdk pake susu
        if "americano" in coffee_item.get_name().lower():
            milk = "None"
        
        # Coffee Milk
        else:
            print("\nPilih jenis susu:")
            milk_options = ["Regular", "Oat milk (+5000)", "Almond milk (+5000)"]
            for i, opt in enumerate(milk_options, 1):
                print(f"{i}. {opt}")
            while True:
                try:
                    milk_choice = int(input("Pilih susu (1-3): "))
                    if 1 <= milk_choice <= 3:
                        milk = milk_options[milk_choice - 1]
                        break
                    else:
                        print("Pilihan tidak tersedia.")
                except ValueError:
                    print("UNVALID. . .")

        # Coffee Cup Size
        print("\nCup Size:")
        size_options = ["Short", "Medium (+3000)", "Tall (+6000)"]
        for i, opt in enumerate(size_options, 1):
            print(f"{i}. {opt}")
        while True:
            try:
                size_choice = int(input("Pilih ukuran (1-3): "))
                if 1 <= size_choice <= 3:
                    size = size_options[size_choice - 1]
                    break
                else:
                    print("Pilihan tidak tersedia.")
            except ValueError:
                print("UNVALID. . .")

        # Coffee sweet 
        sweet_options = ["Less", "Normal", "More"]
        print("\nPilih level gula:")
        for i, opt in enumerate(sweet_options, 1):
            print(f"{i}. {opt}")
        while True:
            try:
                sweet_choice = int(input("Pilih gula (1-3): "))
                if 1 <= sweet_choice <= 3:
                    sweet = sweet_options[sweet_choice - 1]
                    break
                else:
                    print("Pilihan tidak tersedia.")
            except ValueError:
                print("UNVALID. . .")

        # Coffee Ice
        ice_options = ["Less", "Normal", "More"]
        print("\nIce Level:")
        for i, opt in enumerate(ice_options, 1):
            print(f"{i}. {opt}")
        while True:
            try:
                ice_choice = int(input("Pilih es (1-3): "))
                if 1 <= ice_choice <= 3:
                    ice = ice_options[ice_choice - 1]
                    break
                else:
                    print("Pilihan tidak tersedia.")
            except ValueError:
                print("UNVALID. . .")

        coffee_item.set_customization(size, milk, sweet, ice)
        if milk in ["Oat milk (+5000)", "Almond milk (+5000)"]:
            milk_cost = 5000
            coffee_item._price += milk_cost
            print(f"Extra Charge Rp{milk_cost} for {milk} added.")
        size_cost = 0
        if size in ["Medium (+3000)"]:
            size_cost += 3000
            coffee_item._price += size_cost
            print(f"Extra Charge Rp{size_cost} for {size} added.")
        if size in ["Tall (+6000)"]:
            size_cost += 6000
            coffee_item._price += size_cost
            print(f"Extra Charge Rp{size_cost} for {size} added.")

    # Perubahan user pd item Tea
    def customize_tea(self, tea_item: Tea):
        # Tea Cup Size
        print("\nCup Size: ")
        size_options = ["Short", "Medium (+3000)", "Tall (+6000)"]
        for i, opt in enumerate(size_options, 1):
            print(f"{i}. {opt}")
        while True:
            try:
                size_choice = int(input("Pilih ukuran (1-3): "))
                if 1 <= size_choice <= 3:
                    size = size_options[size_choice - 1]
                    break
                else:
                    print("Pilihan tidak tersedia.")
            except ValueError:
                print("UNVALID. . .")

        # Tea Ice
        print("\nIce Level:")
        ice_options = ["Less", "Normal", "More"]
        for i, opt in enumerate(ice_options, 1):
            print(f"{i}. {opt}")
        while True:
            try:
                ice_choice = int(input("Pilih es (1-3): "))
                if 1 <= ice_choice <= 3:
                    ice = ice_options[ice_choice - 1]
                    break
                else:
                    print("Pilihan tidak tersedia.")
            except ValueError:
                print("UNVALID. . .")

        tea_item.set_customization(size, ice)
        size_cost = 0
        if size in ["Medium (+3000)"]:
            size_cost += 3000
            tea_item._price += size_cost
            print(f"Extra Charge Rp{size_cost} for {size} added.")
        if size in ["Tall (+6000)"]:
            size_cost += 6000
            tea_item._price += size_cost
            print(f"Extra Charge Rp{size_cost} for {size} added.")

    # Update user pd order (qty & erase item)
    def update_order(self):
        self.order.display_order(show_index=True)
        try:
            idx = int(input("Pilih nomor item untuk diubah jumlahnya (1, 2, dst): ")) - 1
            if 0 <= idx < len(self.order.cart):
                new_qty = int(input("Masukkan jumlah baru: "))
                if new_qty == 0:
                     removed_item = self.order.cart.pop(idx)
                     print(f"{removed_item[0].get_name()} erased from cart.")
                elif 1 <= new_qty <= 10:
                    self.order.update_item(idx, new_qty)
                    print("Jumlah berhasil diubah.")
                else:
                    print("Max 10 pcs.")
            else:
                print("Item tidak ditemukan.")
        except ValueError:
            print("UNVALID. . .")

    # Asynchronous process utk lama pembuatan
    async def estimate_wait_time(self):
        total_seconds = 0
        for item, qty in self.order.cart:
            # 60 utk 1 detik
            if isinstance(item, Coffee):
                total_seconds += qty * 60       
            elif isinstance(item, Tea):
                total_seconds += qty * 60
            elif isinstance(item, Food):
                total_seconds += qty * 120

        estimated_minutes = total_seconds // 60
        print(f"\nEstimated around {estimated_minutes} minutes for your order...")

        await asyncio.sleep(total_seconds / 60)
        print(f"\n{self.customer.get_name()} your order is ready to take ! :D")

    # Checkout & Nota
    def checkout(self):
        total = self.order.display_order()
        metode = self.payment.choose_method()

        waktu_beli = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print("\n==============================")
        print("          NOTA PEMBELIAN")
        print("==============================")
        print(f"Nama Customer : {self.customer.get_name()}")
        print(f"Waktu         : {waktu_beli}")
        print(f"Metode Bayar  : {metode}")
        print("------------------------------")
        grand_total = 0
        for item, qty in self.order.cart:
            sub_total = item.get_price() * qty
            print(f"{item.get_name()} x{qty} @ Rp{item.get_price():.0f} = Rp{sub_total:.0f}")

            if isinstance(item, Coffee):
                print(f"  -> Size: {item.cup_size}, Milk: {item.milk_type}, sweet: {item.sweet_level}, Ice: {item.ice_level}")
            elif isinstance(item, Tea):
                print(f"  -> Size: {item.cup_size},  Ice: {item.ice_level}")

            grand_total += sub_total
        print("------------------------------")
        print(f"TOTAL DIBAYAR : Rp{grand_total:.0f}")
        print("==============================")
        print("THANK YOU, AND COME AGAIN ! :3 \n")

        asyncio.run(self.estimate_wait_time())


if __name__ == "__main__":
    app = CoffeeShop()
    app.start()
