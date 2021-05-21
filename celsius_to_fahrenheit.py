#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program converts celsius to fahrenheit

def fahrenheit():
    # this function receives a celsius temperature and converts it fahrenheit

    # input
    celsius_as_string = input("Enter a temperature in °C: ")

    # process & output
    try:
        celsius = float(celsius_as_string)
        fahrenheit = (9 / 5) * celsius + 32
        print("{0}°C is equal to {1}°F".format(celsius, fahrenheit))
    except (Exception):
        print("{0} is not a valid celsius temperature".format(
              celsius_as_string))
    finally:
        print("Done.")


def main():
    # this function calls another function

    # call function
    fahrenheit()


if __name__ == "__main__":
    main()
