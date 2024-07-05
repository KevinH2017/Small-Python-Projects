from tkinter import *
import math

root = Tk()
blank_space = " "
root.title("Python Calculator")
root.resizable(width=False, height=False)
root.geometry("480x568+450+90")

# Class to hold functions
class Calc():
    # Functions for math operations
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y