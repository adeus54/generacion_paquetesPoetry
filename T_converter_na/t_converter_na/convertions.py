class Celsius:  

    rankine = 491.67
    fahrenheit = 32
    kelvin = 273.15

    def C_to_R (self, temperature):
        '''  
        
        '''
        TR = 9/5 * (temperature + self.kelvin)
        return TR


    def C_to_F  (self, temperature):
        '''  
        
        '''
        TF = (temperature * 9/5) + self.fahrenheit
        return TF


    def C_to_K  (self, temperature):
        '''  
        
        '''
        TK = temperature + self.kelvin
        return TK


class Fahrenheit:

    rankine = 459.67
    fahrenheit = 32

    def F_to_R (self, temperature):
        '''  
        
        '''
        TR = temperature + self.rankine
        return TR


    def F_to_C  (self, temperature):
        '''  
        
        '''
        TF = (temperature - self.fahrenheit) * 5/9
        return TF


    def F_to_K  (self, temperature):
        '''  
        
        '''
        TK = 5/9 * (temperature + self.rankine)
        return TK


class Kelvin:

    rankine = 459.67
    kelvin = 273.15

    def K_to_R (self, temperature):
        '''  
        
        '''
        TR = (9/5) * temperature
        return TR


    def K_to_C  (self, temperature):
        '''  
        
        '''
        TF = temperature - self.kelvin
        return TF


    def K_to_F  (self, temperature):
        '''  
        
        '''
        TK = (9/5 * temperature) - self.rankine
        return TK


class Rankine:


    def R_to_K (self, temperature):
        '''  
        
        '''
        TR = (5/9) * temperature
        return TR


    def R_to_C  (self, temperature):
        '''  
        
        '''
        TF = 5/9 * (temperature - 491.67)
        return TF


    def R_to_F  (self, temperature):
        '''  
        
        '''
        TK = (9/5 * temperature) - 459.67
        return TK


def main():
    from_celcius = Celsius()
    from_fahrenheit = Fahrenheit()

    print(from_celcius.C_to_F(temperature = 40))
    print(from_celcius.C_to_R(temperature = 40))
    print(from_fahrenheit.F_to_K(temperature = 40))

if __name__ == "__main__":
    main()