print()
print("*Unit Converter*")
print()

conversion_factors = [(1, 'km', 'mi'),
                      (2, 'mi', 'km'),
                      (3, 'kg', 'lb'),
                      (4, 'lbs', 'kg'),
                      (5, 'F', 'C'),
                      (6, 'C', 'F')
                      ]

print("Conversion options:")
print()

for conversion_number, from_unit, to_unit in conversion_factors:
    print(f"{conversion_number}. {from_unit} to {to_unit}")

print()
conversion = input("Choose a conversion (1-6): ")
conversion_number = int(conversion) - 1

conversion_number, from_unit, to_unit = conversion_factors[conversion_number]
print()
from_value = float(input(f'Enter {from_unit} --> '))
print()

if conversion_number == 1:
    to_value = from_value * 0.621371
    print(f'{from_value} {from_unit} --> {to_value} {to_unit}')
elif conversion_number == 2:
    to_value = from_value * 1.60934
    print(f'{from_value} {from_unit} --> {to_value} {to_unit}')
elif conversion_number == 3:
    to_value = from_value * 2.20462
    print(f'{from_value} {from_unit} --> {to_value} {to_unit}')
elif conversion_number == 4:
    to_value = from_value * 0.453592
    print(f'{from_value} {from_unit} --> {to_value} {to_unit}')
elif conversion_number == 5:
    to_value = (from_value - 32) * 5.0/9.0
    print(f'{from_value} {from_unit} --> {to_value} {to_unit}')
elif conversion_number == 6:
    to_value = (from_value * 9.0/5.0) + 32
    print(f'{from_value} {from_unit} --> {to_value} {to_unit}')
