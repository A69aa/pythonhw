chui = float(input("введите температуру воздуха в Чуе:"))
issykkul = float(input(" Иссык-Куле:"))
talas = float(input("введите температуру воздуха в Таласе:"))
jalalabad = float(input("введите температуру воздуха в Джалал Абаде:"))
naryn = float(input("введите температуру воздуха в Нарыне:"))
osh = float(input("введите температуру воздуха в Оше:"))
batken = float(input("введите температуру воздуха в Баткене:"))

vychislenya = ((chui + issykkul + talas + jalalabad + naryn + osh + batken) / 7)
round = round(vychislenya, 4)
print("средний показатель воздуха по КР на сегодня", round, "°C")




