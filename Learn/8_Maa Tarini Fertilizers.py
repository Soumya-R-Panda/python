import os
import json

class Shop:
    def __init__(self):
        self.file_name = "shop_data.json"
        self.debtors_file = "debtors.json"
        self.creditors_file = "creditors.json"
        self.products = {
            1: ("ଚାଉଳ", 25),
            2: ("ପୋଟାସ", 30),
            3: ("ୟୁରିଆ", 10),
            4: ("DAP", 40),
            5: ("ଗ୍ରୋମର", 40)
        }
        self.load_data()
    
    def load_data(self):
        for file in [self.file_name, self.debtors_file, self.creditors_file]:
            if not os.path.isfile(file):
                with open(file, "w") as f:
                    json.dump([], f)
    
    def save_data(self, customers):
        with open(self.file_name, "w") as file:
            json.dump(customers, file, indent=4)
    
    def save_debtor(self, name, phone, amount_due):
        debtors = self.get_data(self.debtors_file)
        debtors.append({"name": name, "phone": phone, "amount_due": amount_due})
        self.save_json_data(self.debtors_file, debtors)
    
    def save_creditor(self, name, phone, extra_amount):
        creditors = self.get_data(self.creditors_file)
        creditors.append({"name": name, "phone": phone, "extra_amount": extra_amount})
        self.save_json_data(self.creditors_file, creditors)
    
    def get_data(self, file_name):
        try:
            with open(file_name, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def save_json_data(self, file_name, data):
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
    
    def get_customers(self):
        return self.get_data(self.file_name)
    
    def add_customer(self):
        name = input("Enter Customer Name: ")
        phone = input("Enter Phone Number: ")
        cart = {}

        print("\nAvailable Products:")
        for num, (product, price) in self.products.items():
            print(f"{num}. {product}: ₹{price} per unit")

        while True:
            try:
                product_num = int(input("Enter product number to buy (or 0 to finish): "))
                if product_num == 0:
                    break
                if product_num in self.products:
                    quantity = int(input(f"Enter quantity for {self.products[product_num][0]}: "))
                    cart[self.products[product_num][0]] = cart.get(self.products[product_num][0], 0) + quantity
                else:
                    print("Invalid product number! Please enter a valid number.")
            except ValueError:
                print("Please enter a valid number.")
        
        total = sum(self.products[num][1] * qty for item, qty in cart.items() for num, (name, price) in self.products.items() if name == item)
        payment = int(input(f"Total Amount: ₹{total}. Enter payment amount: ₹"))
        
        if payment > total:
            extra_amount = payment - total
            print(f"Payment successful! Extra amount recorded: ₹{extra_amount}")
            self.save_creditor(name, phone, extra_amount)
        elif payment == total:
            print("Payment successful! No extra or due amount.")
        else:
            amount_due = total - payment
            print(f"Partial payment received. Amount due: ₹{amount_due}")
            self.save_debtor(name, phone, amount_due)
        
        customers = self.get_customers()
        customers.append({"name": name, "phone": phone, "cart": cart, "total": total})
        self.save_data(customers)
        print("Customer details added successfully!")
    
    def modify_customer(self):
        name = input("Enter the name of the customer to modify: ")
        customers = self.get_customers()
        for customer in customers:
            if customer["name"].lower() == name.lower():
                customer["phone"] = input("Enter new phone number: ") or customer["phone"]
                self.save_data(customers)
                print("Customer details updated successfully!")
                return
        print("Customer not found!")
    
    def delete_customer(self):
        name = input("Enter the name of the customer to delete: ")
        customers = self.get_customers()
        customers = [c for c in customers if c["name"].lower() != name.lower()]
        self.save_data(customers)

        debtors = self.get_data(self.debtors_file)
        debtors = [d for d in debtors if d["name"].lower() != name.lower()]
        self.save_json_data(self.debtors_file, debtors)

        creditors = self.get_data(self.creditors_file)
        creditors = [c for c in creditors if c["name"].lower() != name.lower()]
        self.save_json_data(self.creditors_file, creditors)

        print("Customer deleted successfully!")
    
    def search_customer(self):
        name = input("Enter the name of the customer to search: ")
        customers = self.get_customers()
        for customer in customers:
            if customer["name"].lower() == name.lower():
                print(f"Customer Found: {customer}")
                return
        print("Customer not found!")
    
    def view_all_customers(self):
        customers = self.get_customers()
        if customers:
            for customer in customers:
                print(customer)
        else:
            print("No customer data available.")
    
    def menu(self):
        options = {
            1: {"title": "Add new customer details", "method": self.add_customer},
            2: {"title": "Modify existing customer details", "method": self.modify_customer},
            3: {"title": "Search customer details", "method": self.search_customer},
            4: {"title": "View all customer details", "method": self.view_all_customers},
            5: {"title": "Delete customer details", "method": self.delete_customer},
            6: {"title": "Exit the program", "method": exit}
        }
        
        while True:
            print("\nWelcome to Maa Tarini Fertilizers")
            print("Prop : Rabindra Nath Panda\n")
            for num, option in options.items():
                print(f"{num}: {option['title']}")
            
            try:
                choice = int(input("Enter your choice (1-6): "))
                if choice in options:
                    options[choice]["method"]()
                else:
                    print("Invalid choice! Please enter a number between 1 and 6.")
            except ValueError:
                print("Please enter a valid number.")

if __name__ == "__main__":
    shop = Shop()
    shop.menu()
