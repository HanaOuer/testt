from tkinter import *
from tkinter import ttk, messagebox
import tempfile
from time import strftime
import os

class MyMarket:
    def __init__(self, root):
        self.root = root
        self.root.title("Market")
        self.root.geometry("1300x1100+0+0")

        # Create the title label
        title = Label(
            self.root,
            text="MY MARKET",
            font=("Helvetica", 34, "bold italic"),
            fg="red",
            bg="lightgray"
        )
        title.pack(side=TOP, fill=X)

        # Create a function to update the time
        def update_time():
            current_time = strftime("%H:%M:%S")
            lblheure.config(text=current_time)
            lblheure.after(1000, update_time)

        # Create the time label
        lblheure = Label(self.root, text="HH:MM:SS", font=("Helvetica", 15, "bold"), fg="black")
        lblheure.place(x=0, y=20, width=100, height=45)

        # Start the time update function
        update_time()

        # Create the Main_Frame here
        self.Main_Frame = Frame(self.root, bd=2, relief=GROOVE, bg="gray")
        self.Main_Frame.place(x=20, y=70, width=1200, height=720)

        # Call the create_cart method to create the shopping cart
        self.create_cart()

    def create_cart(self):
        # Create a shopping cart frame
        cart_frame = Frame(self.Main_Frame, bd=2, relief=GROOVE)
        cart_frame.place(x=900, y=10, width=270, height=380)

        # Create a title for the cart
        cart_title = Label(cart_frame, text="Shopping Cart", font=("Helvetica", 20, "bold"))
        cart_title.pack(fill=X)

        # Create a listbox to display cart items
        self.cart_listbox = Listbox(cart_frame, selectbackground="gold", selectmode=SINGLE)
        self.cart_listbox.pack(fill=BOTH, expand=1)

        # Create labels to display item and price
        lbl_item = Label(cart_frame, text="Item", font=("Helvetica", 15, "bold"))
        lbl_item.pack()

        lbl_price = Label(cart_frame, text="Price", font=("Helvetica", 15, "bold"))
        lbl_price.pack()

        # Create a button to add items to the cart
        add_to_cart_btn = Button(cart_frame, text="Add to Cart", command=self.add_to_cart)
        add_to_cart_btn.pack()

        # Create a button to remove items from the cart
        remove_from_cart_btn = Button(cart_frame, text="Remove from Cart", command=self.remove_from_cart)
        remove_from_cart_btn.pack()

        # Create a button to generate and print the bill
        generate_bill_btn = Button(cart_frame, text="Generate Bill", command=self.generate_bill)
        generate_bill_btn.pack()

        # Initialize cart and total cost
        self.cart = []
        self.total_cost = 0.0

    def add_to_cart(self):
        # Add item and price to the cart listbox
        item = "Item Name"  # Replace with the actual item name
        price = 10.0  # Replace with the actual item price
        self.cart_listbox.insert(END, f"{item} - ${price}")
        self.cart.append((item, price))
        self.total_cost += price

    def remove_from_cart(self):
        # Remove selected item from the cart listbox
        selected_item_index = self.cart_listbox.curselection()
        if selected_item_index:
            index = selected_item_index[0]
            item, price = self.cart[index]
            self.cart_listbox.delete(index)
            self.cart.pop(index)
            self.total_cost -= price

    def generate_bill(self):
        # Generate and display the bill in a new window
        bill_window = Toplevel(self.root)
        bill_window.title("Bill")
        bill_window.geometry("400x500")

        # Create a text widget to display the bill content
        bill_text = Text(bill_window, font=("Helvetica", 12))
        bill_text.pack(fill=BOTH, expand=1)

        # Populate the bill content
        bill_text.insert(END, "MY MARKET - BILL\n\n")
        for item, price in self.cart:
            bill_text.insert(END, f"{item}: ${price:.2f}\n")
        bill_text.insert(END, "\nTotal Cost: ${:.2f}".format(self.total_cost))

        # Create a button to print the bill
        print_bill_btn = Button(bill_window, text="Print Bill", command=lambda: self.print_bill(bill_text))
        print_bill_btn.pack()

    def print_bill(self, bill_text_widget):
        # Save the bill content to a temporary file and open it for printing
        temp_file_path = tempfile.mktemp(suffix=".txt")
        with open(temp_file_path, "w") as bill_file:
            bill_file.write(bill_text_widget.get("1.0", END))

        # Open the temporary bill file for printing
        os.system(f"notepad /p {temp_file_path}")

if __name__ == "__main__":
    root = Tk()
    obj = MyMarket(root)
    root.mainloop()
