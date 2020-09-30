# 1 inch = 2.54 cm
# 1 mile = 1.61 km
# 1 lb = 0.4535 kg
# 1 oz = 28.35 g
# 1 am. gallon = 3.785 liters
# 1 eng. pint = 0.5683 liters


results_of_conv_dict = {}
units_dict = {'inch': 2.54,
              'mile': 1.61,
              'lb': 0.4535,
              'oz': 28.35,
              'gallon': 3.785,
              'pint': 0.5683,
              }


# 1.Перевод дюймов в см

def inch_to_cm(number):
    if isinstance(number, int):
        convert_number = units_dict.get('inch') * number
        # results_of_conv_dict['inch_to_cm'] = round(convert_number, 3)
        return convert_number
    else:
        print(f'{number} is not a number.')


# 2.Перевод см в дюймы

def cm_to_inch(number):
    if isinstance(number, int):
        convert_number = number / units_dict.get('inch')
        # results_of_conv_dict['cm_to_inch'] = round(convert_number, 3)
        return convert_number
    else:
        print(f'{number} is not a number.')


# 3.Перевод милей в км

def miles_to_km(number):
    if isinstance(number, int):
        convert_number = number * units_dict.get('mile')
        # results_of_conv_dict['miles_to_km'] = round(convert_number, 3)
        return convert_number
    else:
        print(f'{number} is not a number.')


# 4.Перевод км в мили

def km_to_miles(number):
    if isinstance(number, int):
        convert_number = number / units_dict.get('mile')
        results_of_conv_dict['km_to_miles'] = round(convert_number, 3)
        return convert_number
    else:
        print(f'{number} is not a number.')


# 5.Перевод фунтов в кг

def lb_to_kg(number):
    if isinstance(number, int):
        convert_number = number * units_dict.get('lb')
        results_of_conv_dict['lb_to_kg'] = round(convert_number, 3)
        return convert_number
    else:
        print(f'{number} is not a number.')


# 6.Перевод кг в фунты

def kg_to_lb(number):
    if isinstance(number, int):
        convert_number = number / units_dict.get('lb')
        results_of_conv_dict['kg_to_lb'] = round(convert_number, 3)
        return convert_number
    else:
        print(f'{number} is not a number.')


# 7.Перевод унций в граммы

def oz_to_gram(number):
    if isinstance(number, int):
        convert_number = number * units_dict.get('oz')
        results_of_conv_dict['oz_to_gram'] = round(convert_number, 3)
        return convert_number
    else:
        print(f'{number} is not a number.')


# 8.Перевод грамм в унции

def gram_to_oz(number):
    if isinstance(number, int):
        convert_number = number / units_dict.get('oz')
        results_of_conv_dict['gram_to_oz'] = round(convert_number, 3)
        return convert_number
    else:
        print(f'{number} is not a number.')


# 9.Перевод галлон в литр

def gallon_to_lt(number):
    if isinstance(number, int):
        convert_number = number * units_dict.get('gallon')
        results_of_conv_dict['gallon_to_lt'] = round(convert_number, 3)
        return convert_number
    else:
        print(f'{number} is not a number.')


# 10.Перевод литра в галлон

def lt_to_gallon(number):
    if isinstance(number, int):
        convert_number = number / units_dict.get('gallon')
        results_of_conv_dict['lt_to_gallon'] = round(convert_number, 3)
        return convert_number
    else:
        print(f'{number} is not a number.')


# 11.Перевод пинты в литр

def pint_to_liter(number):
    if isinstance(number, int):
        convert_number = number * units_dict.get('pint')
        results_of_conv_dict['pint_to_liter'] = round(convert_number, 3)
        return convert_number
    else:
        print(f'{number} is not a number.')


# 12.Перевод литра в пинту

def liter_to_pint(number):
    if isinstance(number, int):
        convert_number = number / units_dict.get('pint')
        results_of_conv_dict['liter_to_pint'] = round(convert_number, 3)
        return convert_number
    else:
        print(f'{number} is not a number.')


#

while True:
    user_number = int(input('Choose option to convert (0 - 12): '))
    if user_number == 0:
        break
    elif user_number == 1:
        number_to_convert = int(input('Enter the number to convert inches to cm: '))
        if number_to_convert == 0:
            break
        else:
            print(inch_to_cm(number_to_convert))
    elif user_number == 2:
        number_to_convert = int(input('Enter the number to convert cm to inches: '))
        if number_to_convert == 0:
            break
        else:
            print(cm_to_inch(number_to_convert))
    elif user_number == 3:
        number_to_convert = int(input('Enter the number to convert miles to km: '))
        if number_to_convert == 0:
            break
        else:
            print(miles_to_km(number_to_convert))
    elif user_number == 4:
        number_to_convert = int(input('Enter the number to convert km to miles: '))
        if number_to_convert == 0:
            break
        else:
            print(km_to_miles(number_to_convert))
    elif user_number == 5:
        number_to_convert = int(input('Enter the number to convert lb to kg: '))
        if number_to_convert == 0:
            break
        else:
            print(lb_to_kg(number_to_convert))
    elif user_number == 6:
        number_to_convert = int(input('Enter the number to convert kg to lb: '))
        if number_to_convert == 0:
            break
        else:
            print(kg_to_lb(number_to_convert))
    elif user_number == 7:
        number_to_convert = int(input('Enter the number to convert oz to gram: '))
        if number_to_convert == 0:
            break
        else:
            print(oz_to_gram(number_to_convert))
    elif user_number == 8:
        number_to_convert = int(input('Enter the number to convert gram to oz: '))
        if number_to_convert == 0:
            break
        else:
            print(gram_to_oz(number_to_convert))
    elif user_number == 9:
        number_to_convert = int(input('Enter the number to convert gallon to liters: '))
        if number_to_convert == 0:
            break
        else:
            print(gallon_to_lt(number_to_convert))
    elif user_number == 10:
        number_to_convert = int(input('Enter the number to convert liters to gallon: '))
        if number_to_convert == 0:
            break
        else:
            print(lt_to_gallon(number_to_convert))
    elif user_number == 11:
        number_to_convert = int(input('Enter the number to convert pint to liters: '))
        if number_to_convert == 0:
            break
        else:
            print(pint_to_liter(number_to_convert))
    elif user_number == 12:
        number_to_convert = int(input('Enter the number to convert liters to pint: '))
        if number_to_convert == 0:
            break
        else:
            print(liter_to_pint(number_to_convert))


