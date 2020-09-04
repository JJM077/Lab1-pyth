temp = input("Enter temperature: ")
unit = input("Enter unit in F/f or C/c: ")
temp = float(temp) 
if unit == "F" or unit == "f":
  print(f"{temp}° in Fahrenheit is equivalent to {(temp - 32)/ (9/5)}° Celsius.")


elif unit == "C" or unit == "c":
  print(f"{temp} in Celsius is equivalent to {(temp * (9/5)) + 32}° Fahrenheit.")
else:
    print(f"Invalid unit({unit}).")