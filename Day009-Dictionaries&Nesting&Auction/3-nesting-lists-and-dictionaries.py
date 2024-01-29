# Nesting
captials = {
    "France": "Paris",
    "Germany":"Berlin",
}

# Nesting a List in a Dictionary
# 在字典中嵌套列表
travel_log_lists_in_dictionaries = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting a Dictionary in a Dictionary
# 在字典中嵌套字典
travel_log_dictionaries = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits":  12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits":  5,
    },
}

# Nesting Dictionary in a List
# 在列表中嵌套字典
traval_log_lists = [
    {
        "country":"France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country":"Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]