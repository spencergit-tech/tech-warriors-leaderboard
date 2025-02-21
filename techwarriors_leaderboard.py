import os
import json

class Leaderboard:
    def __init__(self, filename='leaderboard.json'):
        self.scores = {}
        self.filename = filename
        self.load_scores()

    def add_score(self, username, points):
        self.scores[username] = points

    def get_leaderboard(self):
        # Sort the leaderboard by points in descending order
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_scores

    def display_leaderboard(self):
        print("\n" + 
              " _            _                               _                \n" +
              "| |_ ___  ___| |__   __      ____ _ _ __ _ __(_) ___  _ __ ___ \n" +
              "| __/ _ \\/ __| '_ \\  \\ \\ /\\ / / _` | '__| '__| |/ _ \\| '__/ __|\n" +
              "| ||  __/ (__| | | |  \\ V  V / (_| | |  | |  | | (_) | |  \\__ \\ \n" +
              " \\__\\___|\\___|_| |_|   \\_/\\_/ \\__,_|_|  |_|  |_|\\___/|_|  |___/ \n" +
              "\n")
        print("Leaderboard:")
        print("Rank | Username | Points")
        print("-------------------------")
        for rank, (username, points) in enumerate(self.get_leaderboard(), start=1):
            print(f"{rank:<4} | {username:<9} | {points}")

    def save_scores(self):
        with open(self.filename, 'w') as f:
            json.dump(self.scores, f)

    def load_scores(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.scores = json.load(f)

def clear_screen():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    leaderboard = Leaderboard()  # Load existing leaderboard data

    while True:
        # Display replacement information
        print("battery replacement = 5")
        print("mobo replacement = 6")
        print("lcd replacement = 5")
        print("daughterboard replacement = 3")
        print("scrapping = 2")
        
        while True:
            username = input("Enter your username (or type 'exit' to reset, 'quit' to exit, 'view' to see leaderboard): ")
            if username.lower() == 'exit':
                clear_screen()  # Clear the screen
                leaderboard.save_scores()  # Save scores to file
                break
            elif username.lower() == 'quit':
                leaderboard.save_scores()  # Save scores to file before exiting
                print("Exiting the program.")
                return  # Exit the program
            elif username.lower() == 'view':
                leaderboard.display_leaderboard()  # Display current leaderboard
                continue  # Continue to input loop
            
            try:
                points = int(input("Enter your points: "))
                leaderboard.add_score(username, points)
                leaderboard.display_leaderboard()
            except ValueError:
                print("Please enter a valid number for points.")

if __name__ == "__main__":
    main()
