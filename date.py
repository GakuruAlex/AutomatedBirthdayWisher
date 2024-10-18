from datetime import datetime
from pandas import read_csv
class BirthDate:
    def __init__(self):
        self.day =None
        self.month =None
        self.get_date_today()
        self.birth_dates ={}
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

if __name__ == "__main__":
    birthdate = BirthDate()
    birthdate.get_date_today()