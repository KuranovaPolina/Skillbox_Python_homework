class Date:
    def __init__(self):
        self.day = 0
        self.month = 0
        self.year = 0

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        right = True
        day, month, year = date.split('-')
        if int(year) < 0:
            right = False
        elif int(month) < 0 or int(month) > 12:
            right = False
        elif int(day) < 0:
            right = False
        elif int(month) == 2:
            if int(year) % 4 == 0 and int(year) % 400 != 0:
                if int(day) > 29:
                    right = False
            else:
                if int(day) > 28:
                    right = False
        elif int(month) in (4, 6, 9, 11):
            if int(day) > 30:
                right = False
        else:
            if int(day) > 31:
                right = False

        return right

    @classmethod
    def from_string(cls, date: str) -> 'Date':
        day, month, year = date.split('-')
        new_date = Date()
        new_date.day = int(day)
        new_date.month = int(month)
        new_date.year = int(year)
        return new_date

    def __str__(self):
        return f'Day: {self.day} Month: {self.month} Year: {self.year}'


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('31-04-2077'))

# зачтено
