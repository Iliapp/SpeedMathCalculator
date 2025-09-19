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
    submit_button = tk.Button(left_frame, text='Start', command=generate_question)
    submit_button.pack(pady=10)








    #Right FRAME - Calculator
    right_frame = tk.Frame(root,width=200,height=400,background="lightgrey")
    right_frame.pack(side="right", fill="y")





    root.mainloop() # start window
