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


    root.mainloop() # start window
