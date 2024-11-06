import tkinter as tk
from tkinter import messagebox
import random

words = ["apple", "grape", "berry", "lemon", "peach", "melon", "opium", "sigma", "ruski", "blyat", "mango",]

answer = random.choice(words)
attempts = 6
attempt_count = 0

def check_guess():
    global attempt_count
    guess = entry.get().lower()

 
    if len(guess) != 5 or not guess.isalpha():
        messagebox.showerror("Invalid Input", "Please enter a 5-letter word.")
        return

    entry.delete(0, tk.END)

    for i, letter in enumerate(guess):
        if letter == answer[i]:
            color = "green"
        elif letter in answer:
            color = "orange"
        else:
            color = "gray"

        cell = feedback_grid[attempt_count][i]
        cell.config(text=letter.upper(), bg=color, fg="white", font=("Helvetica", 18, "bold"))


    attempt_count += 1
    if guess == answer:
        messagebox.showinfo("Congratulations!", "You guessed the word correctly!")
        root.quit()
    elif attempt_count == attempts:
        messagebox.showinfo("Game Over", f"Sorry, you've used all attempts. The word was '{answer}'.")
        root.quit()

root = tk.Tk()
root.title("Wordle Game")
root.geometry("400x500")
root.config(bg="white")


header = tk.Label(root, text="Guess the 5-letter word!", font=("Helvetica", 16), bg="white")
header.grid(row=0, column=0, columnspan=5, pady=10)


feedback_grid = []
for row in range(attempts):
    row_cells = []
    for col in range(5):
        cell = tk.Label(root, text="", width=4, height=2, relief="solid", bg="light gray")
        cell.grid(row=row + 1, column=col, padx=5, pady=5)
        row_cells.append(cell)
    feedback_grid.append(row_cells)

entry = tk.Entry(root, font=("Helvetica", 16), justify="center")
entry.grid(row=attempts + 2, column=0, columnspan=3, pady=20)


submit_btn = tk.Button(root, text="Submit Guess", command=check_guess, font=("Helvetica", 12))
submit_btn.grid(row=attempts + 2, column=3, columnspan=2)

root.mainloop()
