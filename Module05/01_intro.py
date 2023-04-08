from datetime import date, timedelta

today = date.today() + timedelta(days=-3)
formatted_date = today.strftime("%d.%m.%Y")

print(formatted_date)
