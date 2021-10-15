N = int(input("N = "))
countries = {}

for i in range(N):
    st = input("{0} country:".format(i + 1))
    st_list = st.split(" ")
    countries[st_list[0]] = st_list[1:]

for i in range(3):
    find = False
    city = input("{0} city:".format(i + 1))
    for country in countries.keys():
        if countries[country].count(city) == 1:
            print("City {0} is located in country {1}".format(city, country))
            find = True
            break
    if not find:
        print("No information")

