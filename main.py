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

    entry = tk.Entry(left_frame)
    entry.pack(pady=20)

    score = 0
    src = tk.Label(left_frame,text="Score: 0", font=("Arial", 16), bg="lightblue")
    src.pack(side="top",pady=20)




    def generate_question():
        global global_answer

        difficulty = value_inside.get()


        if difficulty == "Easy":
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
        elif difficulty == "Medium":
            num1 = random.randint(10, 50)
            num2 = random.randint(10, 50)
        elif difficulty == "Hard":
            num1 = random.randint(50, 100)
            num2 = random.randint(50, 100)
        else:
            return


        operators = ["+", "-", "*", "/"]
        operator = random.choice(operators)


        question_text = f"{num1} {operator} {num2}"
        label.config(text=question_text)

        # Обчислюємо правильну відповідь
        if operator == "+":
            correct_answer = num1 + num2
        elif operator == "-":
            correct_answer = num1 - num2
        elif operator == "*":
            correct_answer = num1 * num2
        elif operator == "/":
            correct_answer = round(num1 / num2, 2)

        global_answer = correct_answer
        print(global_answer)


    #button
    button_frame = tk.Frame(left_frame, bg="lightblue")
    button_frame.pack(pady=10)


    def start_game():
        generate_question()
        start_button.pack_forget()  # ховаємо Start
        switch_button.pack()  # з’являється на тому ж місці



    start_button = tk.Button(button_frame, text='Start', command=start_game)
    start_button.pack()

    switch_button = tk.Button(button_frame, text='Switch', command=generate_question)



    def btn_check():

        global score

        user_input = entry.get()
        try:
            user_answer = float(user_input)
        except ValueError:
            print("Please write a number")
            entry.delete(0, tk.END)
            return  # тепер всередині функції

        if user_answer == global_answer:
            print("Correct")
            score += 1
            src.config(text=f"Score: {score}")
        else:
            print("Incorrect")

        entry.delete(0, tk.END)
        generate_question()





    check_button = tk.Button(left_frame, text="Check", command=btn_check)
    check_button.pack(pady=5)















    #Right FRAME - Calculator
    right_frame = tk.Frame(root,width=200,height=400,background="lightgrey")
    right_frame.pack(side="right", fill="y")
    right_frame.pack_propagate(False)




    #Configutation add from inet
    right_frame.grid_rowconfigure(0, weight=5)  # для Label
    right_frame.grid_rowconfigure(1, weight=1)  # для Entry
    right_frame.grid_rowconfigure(2, weight=4)  # для кнопок
    right_frame.grid_columnconfigure(0, weight=1)
    right_frame.grid_columnconfigure(1, weight=1)
    right_frame.grid_columnconfigure(2, weight=1)
    right_frame.grid_columnconfigure(3, weight=1)


    # #GIT push label(add label for calculator)
    cal = tk.Label(right_frame, text="Calculator", font=("Arial", 17), bg="lightgrey")
    cal.grid(row=0, column=0, columnspan=4, pady=5)

    #GIT push input field(add input field for calculator)
    Entry_cal = tk.StringVar(right_frame)
    Entry2 = tk.Entry(right_frame, textvariable=Entry_cal, justify="right", font=("Arial", 18))
    Entry2.grid(row=1, column=0, columnspan=10, padx=2, pady=10, sticky="ew", ipady=10)

    def click_button(num):
        Entry_cal.set(Entry_cal.get() + num)

    def clear():
        Entry_cal.set("")


    def equal():
        try:
            res = str(eval(Entry_cal.get()))
            Entry_cal.set(str(res))
        except Exception:
            Entry_cal.set("Error")


    # Entry_text = Entry_cal.get()
    # print("Enter: +,-,*,/", Entry_text)

    #Buttons GIT PUSH (Buttons)
    buttons = [
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),('/', 2, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),('*', 3, 3),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2),('-', 4, 3),
        ('0', 5, 0), ('.', 5, 1), ('=', 5, 2),('+', 5, 3),
    ]

    for txt, r, c in buttons:
        if txt == "=":
            tk.Button(right_frame, text=txt, width=5, height=2, font=("Arial", 12),
                      command=equal).grid(row=r, column=c, padx=2, pady=2, sticky="nsew")
        else:
            tk.Button(right_frame, text=txt, width=5, height=2, font=("Arial", 12),
                      command=lambda t=txt: click_button(t)).grid(row=r, column=c, padx=2, pady=2, sticky="nsew")

    tk.Button(right_frame, text="Clear", padx=15, pady=5, width=12, command=clear).grid(row=6, column=1, columnspan=2, pady=2)

    # To make the buttons equal in width and height
    for i in range(4):
        right_frame.grid_columnconfigure(i, weight=1)
    for i in range(2, 6):
        right_frame.grid_rowconfigure(i, weight=1)



    root.mainloop() # start window
