from datetime import datetime
from pandas import read_csv
class BirthDate:
    def __init__(self):
        self.day =None
        self.month =None
        self.birthday_names = []
        self.birth_dates ={}
        self.get_date_today()
        self.get_friends_birthdate()
        self.is_today_a_birthday()
    def get_date_today(self)->None:
        today = datetime.fromisoformat(str(datetime.now()))
        self.month, self.day = today.month,today.day
    def get_friends_birthdate(self)->None:
        try:
            data= read_csv("./birthday.csv")
        except FileNotFoundError as e:
            print(f"Error! {e}")
        finally:
            try:
                self.birth_dates = {row.name:[row.month, row.day] for index, row in data.iterrows()}
            except KeyError as error:
                print(f"{error} ")
    def is_today_a_birthday(self)->None:
        for name, birthdate in self.birth_dates.items():
            if birthdate[0] == self.month and birthdate[1] == self.day:
                self.birthday_names.append(name)

if __name__ == "__main__":
    birthdate = BirthDate()
    birthdate.get_date_today()