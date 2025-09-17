import tkinter as tk



if __name__ == '__main__':

    root = tk.Tk()
    root.title("SpeedMath + Calculator")
    root.geometry("800x400")


    #Left FRAME - Game
    left_frame = tk.Frame(root,width=600,height=400,background="lightblue")
    left_frame.pack(side="left", fill="both", expand=True)



    #Right Frame - Calculator
    right_frame = tk.Frame(root,width=200,height=400,background="lightgrey")
    right_frame.pack(side="right", fill="y")





    root.mainloop() # start window
