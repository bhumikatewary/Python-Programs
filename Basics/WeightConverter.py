weight = int(input("Enter weight: "))
unit = input("Enter units: (L) for pounds or (K) for kilograms: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"Converted weight is {converted} kilograms.")
else:
    converted = weight / 0.45
    print(f"Converted weight is {converted} pounds.")

    
