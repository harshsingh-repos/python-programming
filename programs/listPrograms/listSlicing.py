temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]

temps.sort() #changing the orignal list
print(temps)

temp = sorted(temps) #creating a new list temp
print(temp)


cool_temps = temp[:2]
print(cool_temps)
warm_temps = temp[3:]
print(warm_temps)

temps_in_celsius = cool_temps + warm_temps
print(temps_in_celsius)

cool_temps.extend(warm_temps)
print(cool_temps)

