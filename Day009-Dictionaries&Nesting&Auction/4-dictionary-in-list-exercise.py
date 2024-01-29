traval_log = [
    {
        "country":"France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"],
    },
    {
        "country":"Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
    },
]

def add_new_country(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    traval_log.append(new_country)

    #traval_log.append({"country":country,"visits":visits,"cities":cities,})
    

add_new_country("Russia", 2, ["Moscov", "Saint Petersburg"])

print(traval_log)