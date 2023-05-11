import tkinter as tk
from tkinter import messagebox
import sys


def triangular_tower_area():
    print("Please enter the width of the tower:")
    width = int(input())
    print("Please enter the height of the tower:")
    height = int(input())
    if (width % 2 == 0) or (width > 2 * height):
        print("Sorry, but we cannot print your triangular tower model")

    else:
        print("This is the model for your tower: ")
        # Represents the number of times we will have to increase width
        if width == 3:
            print(' *\n' * (height - 1),end="")
            print('***\n')
        else:
            odd1 = (width - 2) // 2
            len_of_width = (height - 2) // odd1

            # If I have a remainder we will have to add as the number of the remainder, rows of the smallest width.
            reminder = (height - 2) % odd1;

            print(('*').rjust((width) // 2 + 1))

            for i in range(3, width, 2):
                if (i == 3):
                    for h in range(reminder):
                        print(('*' * i).rjust((width - i) // 2 + i))
                for j in range(len_of_width):
                    print(('*' * i).rjust((width - i) // 2 + i))
            print('*' * width)


def rectangular_tower_area():
    print("Please enter the width of the tower:")
    width = int(input())
    print("Please enter the height of the tower:")
    height = int(input())

    if abs(width - height < 5):
        print("The area of the building is: ", width * height, '\n\n')
    else:
        print("The perimeter of the building is: ", 2 * (width + height), '\n\n')


def exit_prog():
    sys.exit("We hope you find your tower")


def show_popup():
    popup = tk.Tk()
    popup.title("Twitter Towers ")
    popup.geometry("900x300")

    label = tk.Label(popup,
                     text="Hello, welcome to Twitter towers. Please choose which tower you want to buy, triangular or rectangular.\n"
                          "if you don't want to choose another tower, press 'exit'\n")
    label.pack(pady=20)

    button1 = tk.Button(popup, text="triangular",
                        command=lambda: [popup.destroy(), triangular_tower_area(), show_popup()])
    button1.pack(pady=5)

    button2 = tk.Button(popup, text="rectangular",
                        command=lambda: [popup.destroy(), rectangular_tower_area(), show_popup()])
    button2.pack(pady=5)

    button3 = tk.Button(popup, text="exit", command=exit_prog)
    button3.pack(pady=30)

    popup.mainloop()


show_popup()
