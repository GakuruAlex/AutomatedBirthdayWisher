from datetime import datetime

class BirthDate:
    def __init__(self):
        self.day =None
        self.month =None
    def get_date_today(self):
        today = datetime.fromisoformat(str(datetime.now()))
        self.month, self.day = today.month,today.day

if __name__ == "__main__":
    birthdate = BirthDate()
    birthdate.get_date_today()