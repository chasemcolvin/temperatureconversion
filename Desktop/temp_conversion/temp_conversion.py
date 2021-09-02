#farenheight to celsius conversion
def convert(temp):
    farenheight = float(temp)
    celcius = (farenheight - 32) * .5556
    return celcius 
#I used 100°F (37.778°C) in this example, but you could replace it with any value
print(convert(100))
