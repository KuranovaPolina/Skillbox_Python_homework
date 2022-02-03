import re

text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

own_car = re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', text)
taxi = re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{5,6}', text)

print(own_car)
print(taxi)

# зачтено
