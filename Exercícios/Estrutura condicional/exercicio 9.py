import datetime

date1 = datetime.date.today()
month = date1.month
day = date1.day
year = date1.year

nome = input("Digite seu nome: ")

print(f"Bom dia {nome}, hoje é dia {day} do mês {month} do ano {year}.")
