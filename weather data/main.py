import csv
import pandas

data = pandas.read_csv('weather-data.csv')
temp_celcius = data[data.day == 'Monday'].temp
temp_fahrenheit = (temp_celcius * (9/5)) + 32
print(temp_fahrenheit)