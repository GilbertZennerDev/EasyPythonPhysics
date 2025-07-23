import tkinter as tk
from tkinter import messagebox
import random

#Initializing
class RockPaperScissors:
    def __init__(self, master):
        self.master = master
        master.title("Rock, Paper, Scissors")
        master.geometry("400x300")
        
        self.player_name = ""
        self.player_score = 0
        self.cpu_score = 0
        self.round_count = 0
        
        self.create_start_screen()
#Function for the Start screen
    def create_start_screen(self):
        self.clear_frame()
        
        self.title_label = tk.Label(self.master, text="Rock, Paper, Scissors", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=20)
        
        self.name_label = tk.Label(self.master, text="Enter your name:", font=("Arial", 12))
        self.name_label.pack()
        
        self.name_entry = tk.Entry(self.master, width=30)
        self.name_entry.pack(pady=5)
        
        self.start_button = tk.Button(self.master, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

#Function to start the game
    def start_game(self):
        self.player_name = self.name_entry.get().strip()
        if not self.player_name:
            messagebox.showwarning("Error", "Please enter a name to start.")
            return

        self.player_score = 0
        self.cpu_score = 0
        self.round_count = 0
        self.create_game_screen()

#Function for the game screen
    def create_game_screen(self):
        """Creates the game screen."""
        self.clear_frame()
        
        self.score_label = tk.Label(self.master, text=f"{self.player_name}: 0  |  CPU: 0", font=("Arial", 14))
        self.score_label.pack(pady=10)
        
        self.round_label = tk.Label(self.master, text="Round 1 of 5", font=("Arial", 12))
        self.round_label.pack()
        
        self.choice_label = tk.Label(self.master, text="Choose your move:", font=("Arial", 12))
        self.choice_label.pack(pady=10)
        
        self.player_choice = tk.StringVar(value="rock")
        
        choices_frame = tk.Frame(self.master)
        choices_frame.pack()
        
        tk.Radiobutton(choices_frame, text="Rock", variable=self.player_choice, value="rock").pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(choices_frame, text="Paper", variable=self.player_choice, value="paper").pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(choices_frame, text="Scissors", variable=self.player_choice, value="scissors").pack(side=tk.LEFT, padx=5)
        
        self.play_button = tk.Button(self.master, text="Confirm", command=self.play_round)
        self.play_button.pack(pady=15)
        
        self.result_label = tk.Label(self.master, text="", font=("Arial", 12, "italic"))
        self.result_label.pack()

#main game function
    def play_round(self):
        """Plays a round and evaluates it."""
        player_choice = self.player_choice.get()
        cpu_choice = random.choice(["rock", "paper", "scissors"])
        
        outcome = self.determine_winner(player_choice, cpu_choice)
        
        self.result_label.config(text=f"You chose {player_choice}. CPU chose {cpu_choice}.")
        
        if outcome == "draw":
            messagebox.showinfo("Draw!", "It's a draw! This round will be replayed.")
            return
        elif outcome == "player":
            self.player_score += 1
            messagebox.showinfo("Round Won!", "You won this round!")
        else: # outcome == "cpu"
            self.cpu_score += 1
            messagebox.showinfo("Round Lost", "The CPU won this round.")
        
        self.round_count += 1
        self.update_game_state()

    def determine_winner(self, player, cpu):
        """Determines the winner of a round."""
        if player == cpu:
            return "draw"
        if (player == "rock" and cpu == "scissors") or \
           (player == "scissors" and cpu == "paper") or \
           (player == "paper" and cpu == "rock"):
            return "player"
        return "cpu"

    def update_game_state(self):
        """Updates the score display and checks for game end."""
        self.score_label.config(text=f"{self.player_name}: {self.player_score}  |  CPU: {self.cpu_score}")
        
        if self.round_count >= 5:
            self.end_game()
        else:
            self.round_label.config(text=f"Round {self.round_count + 1} of 5")

    def end_game(self):
        """Displays the game winner and offers a restart button."""
        self.clear_frame()
        
        final_message = ""
        if self.player_score > self.cpu_score:
            final_message = f"Congratulations, {self.player_name}! You won the game!"
        elif self.cpu_score > self.player_score:
            final_message = "Too bad, you lost to the CPU."
        else:
            final_message = "The game ended in a draw!"
            
        self.final_label = tk.Label(self.master, text=final_message, font=("Arial", 16, "bold"), wraplength=350)
        self.final_label.pack(pady=30)
        
        self.new_game_button = tk.Button(self.master, text="New Game", command=self.create_start_screen)
        self.new_game_button.pack(pady=10)

    def clear_frame(self):
        """Removes all widgets from the current window."""
        for widget in self.master.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()

if __name__ == "__main__":
    main()
