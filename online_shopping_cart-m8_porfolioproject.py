class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description=""):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"|\t{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}\t\t")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

    def get_total_cost(self):
        return self.item_price * self.item_quantity

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)
        print('------------------------')
        print('---Item added to Cart---')
        print('------------------------')

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                print('----------------------------')
                print('---Item removed from Cart---')
                print('----------------------------')
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_modify):
        found = False
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                    print('---------------------------')
                    print('---Item quantity changed---')
                    print('---------------------------')
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.get_total_cost() for item in self.cart_items)

    def print_total(self):
        print('-------------------------------------------------')
        print(f"|\t{self.customer_name}'s Shopping Cart - {self.current_date}\t|")
        print(f"|\tNumber of Items: {self.get_num_items_in_cart()}\t\t\t|")
        if not self.cart_items:
            print("|\tSHOPPING CART IS EMPTY\t\t\t|")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"|\tTotal: ${self.get_cost_of_cart()}\t\t\t\t|")
        print('-------------------------------------------------')

    def print_descriptions(self):
        found = False
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()
            found = True
        if found == False:
            print('-------------------')
            print('---Cart is Empty---')
            print('-------------------')

def print_menu(cart):
    menu = (
        "MENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
        "\nChoose an option:"
    )
    
    while True:
        print(menu)
        option = input()
        if option == 'a':
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(item)
        elif option == 'r':
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove: ")
            cart.remove_item(item_name)
        elif option == 'c':
            print("CHANGE ITEM QUANTITY")
            item_name = input("Enter the item name: ")
            item_quantity = int(input("Enter the item quantity: "))
            item_to_modify = ItemToPurchase(item_name, item_price,item_quantity,item_description)
            cart.modify_item(item_to_modify)
        elif option == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif option == 'o':
            print("OUTPUT SHOPPING CART")
            cart.print_total()
        elif option == 'q':
            break
        else:
            print('Invalid option, please type Valid option')

def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)

if __name__ == "__main__":
    main()