from date import BirthDate
from letter import Letter
from send_mail import SendMail
def main()->None:
    """_Create SendMail, Letter and BirthDate objects and run their methods_
    """
    sendmail = SendMail()
    letter = Letter()
    birthdate = BirthDate()
    if len(birthdate.birthday_names) > 0:
        for name in birthdate.birthday_names:
            letter.replace_name(name)
            sendmail.send_mail(message=f"Subject:Happy Birthday\n\n{letter.letter}")
            print(f"Email sent to {name}")

if __name__ == "__main__":
    main()