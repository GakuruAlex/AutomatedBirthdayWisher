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
        """_Get todays date and format it into month and day_
        """
        today = datetime.fromisoformat(str(datetime.now()))
        self.month, self.day = today.month,today.day
    def get_friends_birthdate(self)->None:
        """_Read birthday csv file and populate birth_dates dict with name as key and
            birthday date as value in form of a list_
        """
        try:
            data= read_csv("./birthdays.csv")
        except FileNotFoundError as e:
            print(f"Error! {e}")
        finally:
            try:
                self.birth_dates = {row['name']:[row.month, row.day] for index, row in data.iterrows()}
            except (KeyError, UnboundLocalError) as error:
                print(f"{error} ")
    def is_today_a_birthday(self)->None:
        """_Check if anyone birthday falls on today's date and month and add their name to a list of people to send wishes to_
        """
        for name, birthdate in self.birth_dates.items():
                if birthdate[0] == self.month and birthdate[1] == self.day:
                    self.birthday_names.append(name)

if __name__ == "__main__":
    birthdate = BirthDate()
    birthdate.get_date_today()