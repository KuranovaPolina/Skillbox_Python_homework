N = int(input("N = "))
countries = {}

for i in range(N):
    st = input("{0} country:".format(i + 1))
    st_list = st.split(" ")
    countries[st_list[0]] = st_list[1:]

for i in range(3):
    city = input("{0} city:".format(i + 1))
    for country in countries.keys():
        if countries[country].count(city) == 1:
            print("City {0} is located in country {1}".format(city, country))
        elif countries[country].count(city) == 0:
            print("No information")

# TODO: Лишние и некорректные print'ы:
"""
N = 2
1 country:Россия Москва Питер
2 country:Испания Барса Мадрид
1 city:Барса
No information
City Барса is located in country Испания
2 city:Москва
City Москва is located in country Россия
No information
3 city:Лондон
No information
No information
"""