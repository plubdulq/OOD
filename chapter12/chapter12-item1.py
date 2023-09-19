print(" *** Wind classification *** ")
wind_speed = float(input("Enter wind speed (km/h) : "))
if wind_speed < 0:
    print("!!!Wrong value can't classify.")
else:
    if wind_speed>=209:
        storm_lvl = 'Super Typhoon'
    elif wind_speed >= 102:
        storm_lvl = 'Typhoon'
    elif wind_speed >= 56:
        storm_lvl = 'Tropical Storm'
    elif wind_speed >= 52:
        storm_lvl = 'Depression'
    else:
        storm_lvl = 'Breeze'
    print(f'Wind classification is {storm_lvl}.')