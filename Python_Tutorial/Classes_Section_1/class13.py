weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == 'L':
    weight*=0.45
    weight = round(weight)
    unit = 'kilogram'
else:
    weight/=0.45
    weight = round(weight)
    unit = 'pound'
print(f"You are {weight} {unit}s.")