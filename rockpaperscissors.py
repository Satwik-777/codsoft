import tkinter as tk
from tkinter import messagebox
import random


bg_color = '#34495e'
btn_color = '#f39c12'
text_color = '#ecf0f1'


app = tk.Tk()
app.geometry('400x500')
app.configure(bg=bg_color)


def get_user_input():
    return user_input.get()

def verify_user_input():
    user_choice = get_user_input()
    if user_choice == 'rock' or user_choice == 'paper' or user_choice == 'scissors':
        play_game(user_choice)
    else:
        messagebox.showerror('Invalid Input', 'Please enter either rock, paper, or scissors')

def play_game(user_choice):
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = 'It\'s a tie!'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'scissors' and computer_choice == 'paper') or \
        (user_choice == 'paper' and computer_choice == 'rock'):
        result = 'You win!'
    else:
        result = 'You lose!'

    show_result(result, user_choice, computer_choice)

def show_result(result, user_choice, computer_choice):
    result_text.config(text=result)
    user_choice_text.config(text=user_choice)
    computer_choice_text.config(text=computer_choice)


user_input_label = tk.Label(app, text='Enter your choice:', bg=bg_color, fg=text_color)
user_input_label.pack(pady=20)

user_input = tk.Entry(app)
user_input.pack(pady=10)

submit_button = tk.Button(app, text='Submit', command=verify_user_input, bg=btn_color, fg=text_color)
submit_button.pack(pady=20)

result_text = tk.Label(app, text='', bg=bg_color, fg=text_color)
result_text.pack(pady=20)
user_choice_text = tk.Label(app, text='', bg=bg_color, fg=text_color)
user_choice_text.pack(pady=10)
computer_choice_text = tk.Label(app, text='', bg=bg_color, fg=text_color)
computer_choice_text.pack(pady=10)

app.mainloop()