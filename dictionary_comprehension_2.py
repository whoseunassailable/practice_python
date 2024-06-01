weather_c = eval(input())
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {}
list_of_keys = []
list_of_converted_values = []


for temp_c in weather_c.values():
    temp_f = (temp_c * 9/5) + 32
    list_of_converted_values.append(temp_f)

for key in weather_c.keys():
    list_of_keys.append(key)
    
for i in range(0, len(weather_c)):
    weather_f[list_of_keys[i]] = list_of_converted_values[i]

print(weather_f)