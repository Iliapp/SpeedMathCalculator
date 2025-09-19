import tkinter as tk
import random


if __name__ == '__main__':

    root = tk.Tk()
    root.title("SpeedMath + Calculator")
    root.geometry("800x400")


    #Left FRAME - Game
    left_frame = tk.Frame(root,width=600,height=400,background="lightblue")
    left_frame.pack(side="left", fill="both", expand=True)

    #Diffuculty levels
    label = tk.Label(left_frame,text="Chose Difficulty and Start",font=("Arial", 16), bg="lightblue")
    label.pack(pady=20)

    options_list = ["Easy", "Medium", "Hard"]
    value_inside = tk.StringVar(left_frame)
    value_inside.set("")

    question_menu = tk.OptionMenu(left_frame,value_inside, *options_list)
    question_menu.pack(pady=10) # or grid


















    #Right FRAME - Calculator
    right_frame = tk.Frame(root,width=200,height=400,background="lightgrey")
    right_frame.pack(side="right", fill="y")





    root.mainloop() # start window
