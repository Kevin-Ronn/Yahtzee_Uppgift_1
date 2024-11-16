from die import Die

class YahtzeeGame:
    def __init__(self):
        self.dice = [Die() for _ in range(5)]
        self.keep_playing = True

    def play(self):
        print("Welcome to Yahtzee!")
        while self.keep_playing:
            self.play_round()

    def play_round(self):
        for turn in range(1, 4):
            print(f"Turn {turn} of 3: Rolling dice...")
            for i, die in enumerate(self.dice):
                die.DieRoll()
                print(f"Die {i}: {die}")

            if self.check_yahtzee():
                print(f"You got YAHTZEE! All dice show {self.dice[0].value}.")
                return
            
            if turn < 3 and input("Roll again? (y to continue, any other key to stop): ").lower() != "y":
                break

        if input("Game over! Play again? (y to restart, any other key to quit): ").lower() != "y":
            self.keep_playing = False

    def check_yahtzee(self):
        return all(die.value == self.dice[0].value for die in self.dice)

def main():
    game = YahtzeeGame()
    game.play()

if __name__ == "__main__":
    main()
