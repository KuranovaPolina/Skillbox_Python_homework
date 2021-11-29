class Property:
    def __init__(self, worth):
        self.worth = worth

    def taxes(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def taxes(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def taxes(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def taxes(self):
        return self.worth / 500


def print_info(property, money):
    print(f"Tax {property.taxes()}")

    if money < (property.taxes() + property.worth):
        print(f"You need collect {property.taxes() + property.worth - money}")


all_money = int(input("Input count of your money: "))
cost = int(input("Input cost of your properties: "))
property1 = int(input("Choose property (1 - apartment, 2 - car, 3 - country house) "))

if property1 == 1:
    apartment = Apartment(cost)
    print_info(apartment, all_money)
elif property1 == 2:
    car = Car(cost)
    print_info(car, all_money)
elif property1 == 3:
    countryHouse = CountryHouse(cost)
    print_info(countryHouse, all_money)

# зачтено
