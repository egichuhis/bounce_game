import sys


def moon_weight():
        print('Enter your current earth weight: ')
        weight_earth = int(sys.stdin.readline())
        print('Enter the approximate annual weight increase: ')
        increase = float(sys.stdin.readline())
        print('Enter the number of years to calculate: ')
        years = int(sys.stdin.readline())
        print()

        for x in range(1, years + 1):
            weight_earth = weight_earth + 1
            weight_moon = weight_earth * increase
            print('Weight on moon, Year %s: %s ' % (x, weight_moon))


moon_weight()