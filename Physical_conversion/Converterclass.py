class Converter: 
    conversion_history = []

    @staticmethod
    def temperature_conversion(sub_option, temperature):
        if sub_option in [1, 3]:  
            if temperature < -273.15:
                raise ValueError('The temperature cannot be below absolute zero (-273.15°C).')
        elif sub_option in [4, 5, 6]:  # Kelvin
            if temperature < 0:
                raise ValueError('The temperature in Kelvin cannot be negative.')

        if sub_option == 1:
            Fahrenheit = (temperature * 1.8) + 32
            return f"{temperature}°C is equivalent to {round(Fahrenheit,2)}°F"
        elif sub_option == 2 :
            Celsius = (temperature - 32) / 1.8 
            return f"{temperature}°F is equivalent to {round(Celsius,2)}°C "
        elif sub_option == 3:
            Kelvin = temperature + 273.15
            return f"{temperature}°C is equivalent to {round(Kelvin, 2)} K"
        elif sub_option == 4:
            Celsius = temperature - 273.15
            return f"{temperature} K is equivalent to {round(Celsius, 2)}°C"
        elif sub_option == 5:
            Kelvin = (temperature - 32) / 1.8 + 273.15
            return f"{temperature}°F is equivalent to {round(Kelvin, 2)}K"
        elif sub_option == 6:
            Fahrenheit = (temperature - 273.15) * 1.8 + 32
            return f"{temperature} K is equivalent to {round(Fahrenheit, 2)}°F"
        result = Converter.temperature_conversion(sub_option, temperature)
        Converter.add_to_history(f"Temperature conversion: {result}")
    
    @staticmethod
    def convert_measurements(sub_option,misure,unit_measure_from,unit_measure_to):
        match sub_option:
            case 1:
                units = {
                    'km': 1000,
                    'hm': 100,
                    'dam': 10,
                    'm': 1,
                    'dm' : 0.1,
                    'cm': 0.01,
                    'mm': 0.001,
                    'in': 0.0254,
                    'ft': 0.3048} 

                if unit_measure_from not in units:
                    raise ValueError("Unit unknown: {}".format(unit_measure_from))

                metres = misure * units[unit_measure_from]

                if unit_measure_to in units:
                    return metres / units[unit_measure_to]
                else:
                    raise ValueError("Unit unknown: {}".format(unit_measure_to))
            case 2:
                units = {
                    'm^3': 1000, 
                    'kl': 1000,
                    'hl': 100,    
                    'dal': 10,     
                    'l': 1,        
                    'dl': 0.1,    
                    'cl': 0.01,   
                    'ml': 0.001 
                }
                if unit_measure_from not in units:
                    raise ValueError("Unit unknown: {}".format(unit_measure_from))

                metres = misure * units[unit_measure_from]

                if unit_measure_to in units:
                    return metres / units[unit_measure_to]
                else:
                    raise ValueError("Unit unknown: {}".format(unit_measure_to))
            
            case 3:
                units = {
                    'kg': 1000,   
                    'hg': 100,  
                    'dag': 10,  
                    'g': 1,     
                    'dg': 0.1,  
                    'cg': 0.01, 
                    'mg': 0.001
                }
                if unit_measure_from not in units:
                    raise ValueError("Unit unknown: {}".format(unit_measure_from))

                metres = misure * units[unit_measure_from]

                if unit_measure_to in units:
                    return metres / units[unit_measure_to]
                else:
                    raise ValueError("Unit unknown: {}".format(unit_measure_to))
            case 4:
                units = {
                    's': 1,        
                    'min': 60,    
                    'h': 3600,    
                    'd': 86400,   
                    'wk': 604800, 
                    'mo': 2592000,   
                    'yr': 31536000    
                }
                if unit_measure_from not in units:
                    raise ValueError("Unit unknown: {}".format(unit_measure_from))

                metres = misure * units[unit_measure_from]

                if unit_measure_to in units:
                    return metres / units[unit_measure_to]
                else:
                    raise ValueError("Unit unknown: {}".format(unit_measure_to))
            
            case 5:
                units = {
                'Pa': 1,               
                'kPa': 1000,
                'MPa': 1e6,           
                'bar': 100000,         
                'atm': 101325,        
                }
                if unit_measure_from not in units:
                    raise ValueError("Unit unknown: {}".format(unit_measure_from))

                metres = misure * units[unit_measure_from]

                if unit_measure_to in units:
                    return metres / units[unit_measure_to]
                else:
                    raise ValueError("Unit unknown: {}".format(unit_measure_to))
            
            case 6:  
                units = {
                    'm/s': 1,
                    'km/h': 3.6,  
                    'mph': 2.23694  
                }
                if unit_measure_from not in units:
                    raise ValueError("Unit unknown: {}".format(unit_measure_from))
                
                base_speed = misure / units[unit_measure_from]

                if unit_measure_to in units:
                    return base_speed * units[unit_measure_to]
                else:
                    raise ValueError("Unit unknown: {}".format(unit_measure_to))
       
    @staticmethod
    def add_to_history(conversion):
        Converter.conversion_history.append(conversion)
        print(f"Added to history: {conversion}")

    @staticmethod
    def show_history():
        if not Converter.conversion_history:
            print("No conversion history available.")
        else:
            print("Conversion History:")
            for conversion in Converter.conversion_history:
                print(conversion)