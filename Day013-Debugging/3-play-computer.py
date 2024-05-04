# Play Computer
# 由于两个判断中 要么大于 1994 要么小于 1994，将会导致 1994年的情况没有判断到
# 需要将 elif year > 1994 改为 elif year >= 1994
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")