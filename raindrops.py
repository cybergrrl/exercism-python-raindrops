def convert(number):
    rain_string = ""

    if number % 3 == 0:
        rain_string += "Pling"
    if number % 5 == 0:
        rain_string += "Plang"
    if number % 7 == 0:
        rain_string += "Plong"
    
    if rain_string == "":
        return str(number)
    else: return rain_string

    return rain_string
