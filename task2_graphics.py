import tkinter as tk
import random

class GenerateNumber:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")
        self.root.geometry("500x400")
        self.root.config(bg="#282C34")
        
        self.guess = random.randint(1, 1000)
        self.attempt = 0
        
        self.label = tk.Label(root, text="******* GUESSING GAME *******", 
                              font=("Helvetica", 18, "bold"), fg="#61AFEF", bg="#282C34")
        self.label.pack(pady=20)
        
        self.input_label = tk.Label(root, text="ENTER YOUR GUESSING NUMBER:",
                                    font=("Helvetica", 14), fg="#98C379", bg="#282C34")
        self.input_label.pack()
        
        self.entry = tk.Entry(root, font=("Helvetica", 14), width=10, fg="#282C34", bg="#ABB2BF")
        self.entry.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", font=("Helvetica", 14), fg="#E06C75", bg="#282C34")
        self.result_label.pack(pady=10)
        
        self.button = tk.Button(root, text="Submit", font=("Helvetica", 14), fg="#282C34", bg="#98C379", command=self.check_guess)
        self.button.pack(pady=10)
        
        self.reset_button = tk.Button(root, text="Reset", font=("Helvetica", 12), fg="#282C34", bg="#E06C75", command=self.reset_game)
        self.reset_button.pack(pady=5)

    def check_guess(self):
        try:
            number = int(self.entry.get())
            self.attempt += 1
            
            if number > self.guess:
                self.result_label.config(text='YOUR GUESS IS TOO HIGH !!!! TRY AGAIN!')
            
            elif number < self.guess:
                self.result_label.config(text='YOUR GUESS IS TOO LOW !!!! PLEASE TRY AGAIN!')
            
            elif number == self.guess:
                self.result_label.config(text=f'CONGRATULATIONS !! YOU HAVE GUESSED THE NUMBER IN {self.attempt} ATTEMPTS')
                self.entry.config(state='disabled')
                self.button.config(state='disabled')
        
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
    
    def reset_game(self):
        self.guess = random.randint(1, 1000)
        self.attempt = 0
        self.result_label.config(text="")
        self.entry.config(state='normal')
        self.button.config(state='normal')
        self.entry.delete(0, 'end')

# Creating the main window and running the application
root = tk.Tk()
app = GenerateNumber(root)
root.mainloop()
