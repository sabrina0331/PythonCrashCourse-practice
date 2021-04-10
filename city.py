from city_function import describe_city

while True:
    city = input('Please provide a city name: ')
    if city == 'q':
        break
    country = input('Please provide a country name: ')
    if country == 'q':
        break
    population = input('Please provide a population number: ')
    if population == 'q':
        break
    full_info = describe_city(city,country,population)
    print(full_info)