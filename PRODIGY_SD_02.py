#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67


def main():
    print("Temperature Conversion Program")
    print("Available units: Celsius (C), Fahrenheit (F), Kelvin (K)")

    # Input temperature and unit from the user
    temperature = float(input("Enter the temperature value: "))
    original_unit = input("Enter the original unit (C/F/K): ").upper()

    # Initialize variables for converted temperatures
    celsius = fahrenheit = kelvin = None

    # Perform conversions based on the original unit
    if original_unit == 'C':
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
    elif original_unit == 'F':
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
    elif original_unit == 'K':
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
    else:
        print("Invalid unit. Please enter C, F, or K.")
        return

    # Display the converted temperatures
    print(f"{temperature} {original_unit} is equal to:")
    if celsius is not None:
        print(f"{celsius} C")
    if fahrenheit is not None:
        print(f"{fahrenheit} F")
    if kelvin is not None:
        print(f"{kelvin} K")


if __name__ == "__main__":
    main()


# In[ ]:




