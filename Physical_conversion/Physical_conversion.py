from Converterclass import Converter
menu = '''
    1 Converting your temperature
    2 Convert the measurement
    3 Show conversion history
    0 Quitting the programme'''
print('''Welcome to the physical conversion programme! Are you ready to explore the world of units of measurement? 
Select an option below to start your conversions!''')
print('-'*50)
print(f'{menu}')
print('-'*50)

while True:
    option = input('Please enter the function:\n')
    match option:
        case '1':
            print('''What do you want to convert?
                    1 Celsius (C) to Fahrenheit (F)
                    2 Fahrenheit (F) to Celsius (C)
                    3 Celsius (C) to Kelvin (K)
                    4 Kelvin (K) to Celsius (C)
                    5 Fahrenheit (F) in Kelvin (K)
                    6 Kelvin (K) in Fahrenheit (F)''')
            sub_option = int(input("Please enter the mode:\n"))
            if sub_option < 1 and sub_option > 6:
                print('The category doesn\'t exist')
            else:
                temperature = int(input('Please enter the temperature:\n'))
                result = Converter.temperature_conversion(sub_option,temperature)
                Converter.add_to_history(f"Temperature conversion: {result}")
                print(result)
                print('-'*50)
                
        case '2':
            print('''What do you want to convert?
                    1 metres
                    2 litres
                    3 grams
                    4 time
                    5 pressure 
                    6 speed''')
            sub_option = int(input("Please enter the mode:\n"))
            if sub_option < 1 and sub_option > 6:
                print('The category doesn\'t exist')
            else:
                if sub_option:
                    misure = int(input('Please enter the misure:\n'))
                    unit_measure_from = (input('Please enter your unit measure:\n')) 
                    unit_measure_to = (input('Please enter your desired unit of measurement:\n'))
                    result= Converter.convert_measurements(sub_option,misure,unit_measure_from,unit_measure_to)
                    Converter.add_to_history(f"{misure} {unit_measure_from} = {result} {unit_measure_to}")
                    print(result)
                    print('-'*50)
        
        case '3':
            Converter.show_history()
        
        case '0':
            print('Quitting the programme')
            break
        
        case _:
            print('Invalid option, please try again.')