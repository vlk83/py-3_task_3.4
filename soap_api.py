import osa


############################################################################################################
# Задача №1

def fahrenheit_to_celsius(value):
    URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
    client = osa.client.Client(URL)
    response = client.service.ConvertTemp(Temperature=value, FromUnit='degreeFahrenheit', ToUnit='degreeCelsius')
    return response

def average_temperature(file):
    with open(file, 'r', encoding='utf8') as f:
        temps_celsius=[]
        line = f.readline()
        while line:
            temp = fahrenheit_to_celsius(float(line.replace('F', '').strip()))
            temps_celsius.append(temp)
            line = f.readline()
        average_temperature = sum(temps_celsius) / len(temps_celsius)

    return average_temperature

print('Cредняя за неделю температура по Цельсию:', end=' ')
print(round(average_temperature('temps.txt'), 2))

############################################################################################################
# Задача №2

def convert_to_RUB(value, currency):
    URL = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
    client = osa.client.Client(URL)
    response = client.service.ConvertToNum(toCurrency='RUB', fromCurrency=currency, amount=value, rounding=True)
    return response

def money_for_journey(file):
    with open(file, 'r', encoding='utf8') as f:
        money_list=[]
        line = f.readline()
        while line:
            value = float(line.split(' ')[1])
            currency = line.split(' ')[2].strip()
            money_for_flight = convert_to_RUB(value, currency)
            money_list.append(money_for_flight)
            line = f.readline()
        money_for_journey = int(round(sum(money_list) + 0.5, 0))
    return money_for_journey

print('Количество денег на путешествие в рублях:', end=' ')
print(money_for_journey('currencies.txt'))

############################################################################################################
# Задача №3

def miles_to_kilometres(value):
    URL = 'http://www.webservicex.net/length.asmx?WSDL'
    client = osa.client.Client(URL)
    response = client.service.ChangeLengthUnit(LengthValue=value, fromLengthUnit='Miles', toLengthUnit='Kilometers')
    return response

def journey_total_distance(file):
    with open(file, 'r', encoding='utf8') as f:
        journey_distance_list=[]
        line = f.readline()
        while line:
            value = float(line.split(' ')[1].replace(',', ''))
            journey_distance = miles_to_kilometres(value)
            journey_distance_list.append(journey_distance)
            line = f.readline()
        journey_total_distance = round(sum(journey_distance_list), 2)
    return journey_total_distance

print('Cуммарное расстояние пути в километрах с точностью до сотых:', end=' ')
print(journey_total_distance('travel.txt'))

############################################################################################################
