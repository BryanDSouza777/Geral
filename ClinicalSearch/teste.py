from datetime import datetime


from datetime import date
def calculateAge(birthDate):
    days_in_year = 365.2425
    age = int((date.today() - birthDate).days / days_in_year)
    return age
print(calculateAge(date(2006, 7, 10)), "anos")



'''text = '123@123.com'
check = '@'

if check in text:
    print('ok')
else: print('não')'''