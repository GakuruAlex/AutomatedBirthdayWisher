from random import randint

class Letter:
    def __init__(self):
        self.letter = None
        self.get_letter()
        self.format_letter()
    def get_letter(self)-> None:
        """_Chose a random int among 1 and 3 to represent the letter to chose , open letter templates
            and read content of the letter_
        """
        chosen = randint(1, 3)
        try:
            with open(file=f"./letter_templates/letter_{chosen}.txt") as file:
                self.letter = file.readlines()
        except FileNotFoundError as missing_file:
            print(f"Error {missing_file}")
    def replace_name(self, name: str)-> None:
        """_Replace the [NAME] placeholder in the letter txt file with a given name_

        Args:
            name (str): _Name to replace '[NAME]' with_
        >>>Example
            letter_object.replace_name('John")
            output: Hello John, ...
        """
        self.letter=self.letter.replace("[NAME]", name)
    def format_letter(self)->None:
        """_Given a list as instance variable, join the str in the list_
        """
        new_letter = self.letter[:]
        self.letter="".join(new_letter)

if __name__ == "__main__":
    letter = Letter()