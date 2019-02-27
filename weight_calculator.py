weight_earth = 65

for x in range(1, 16):
    weight_earth = weight_earth + 1
    weight_moon = weight_earth * 0.165
    print('Weight on moon, Year %s: %s ' % (x, weight_moon))

