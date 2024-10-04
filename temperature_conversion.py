def main():
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit (C/F)? ")
        if unit == "C" or unit == "F":
            break
        else: 
            print("Please enter a valid option: C or F")
    try:
        temperature = int(input("Enter the temperature: "))
    except ValueError:
        print("Invalid Input, try a valid temperature")
        temperature = None
    if temperature != None:
        converted_temperature = temperature_conversion(unit, temperature)
        print(converted_temperature)
    
def temperature_conversion(unit, temperature):
    if unit == "C":
        temperature = temperature*9/5+32
    elif unit == "F":
        temperature = (temperature-32)*5/9
    return round(temperature, 0)

if __name__ == "__main__":
    main()