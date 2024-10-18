from random import randint
class Letter:
    def __init__(self):
        self.letter = None
        self.get_letter()
    def get_letter(self):
        chosen = randint(1, 3)
        try:
            with open(file=f"./letter_templates/letter_{chosen}.txt") as file:
                self.letter = file.readlines()
        except FileNotFoundError as missing_file:
            print(f"Error {missing_file}")

if __name__ == "__main__":
    letter = Letter()