from random import randint
import abc
from abc import ABC


class CowsAndBullsBase(ABC):
    def __init__(self):
        self.cows = 0
        self.bulls = 0
        self.number = None
        self.tries = 0

    def generate_num(self):
        num = ""
        while len(num) < 4:
            digit = randint(0, 9)
            if str(digit) not in num:
                num += str(digit)

        self.number = num

    def present(self):
        return f"cows: {self.cows} and bulls: {self.bulls}\n"

    @staticmethod
    def user_guess():
        guess = input("guess the number ")
        if not guess.isdigit() or len(guess) != 4:
            raise ValueError("wrong value for guessing")

        return guess

    def reset_values(self, hard=False):
        self.cows, self.bulls = 0, 0
        self.tries += 1
        if hard:
            self.generate_num()
            self.tries = 0

    def check(self, guess):
        if guess == self.number:
            self.cows = 4
            return

        for i in range(4):
            if guess[i] in self.number:
                if guess[i] == self.number[i]:
                    self.cows += 1
                else:
                    self.bulls += 1

    def won(self):
        print(f"{self.present()}\n------{self.number}------\nYou have tried {self.tries} times\n")

    @abc.abstractmethod
    def play(self):
        pass


class NewGame(CowsAndBullsBase):
    def play(self):
        print('Lets start a game: ')
        self.generate_num()
        while self.cows != 4:
            user_guess = self.user_guess()
            self.check(user_guess)
            if self.cows == 4:
                print(self.present())
                self.won()
                new_game = input('Do you want to play again?: ')
                if new_game == 'yes':
                    self.reset_values()
                else:
                    print('The game is over, it was awesome')
            else:
                print(self.present())
                with open('cows and bulls.txt', 'a') as cb:
                    cb.write(self.present())

                self.reset_values()


game = NewGame()
game.play()
