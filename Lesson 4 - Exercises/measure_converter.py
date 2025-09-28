
class Length:
    def __init__(self, value: float, system: str):
        """
        Constructor
        :param value: numeric measure to convert (up to two decimals expected)
        :param system: 'Metric' for centimeters, 'Imperial' for inches
        """
        self.value = round(float(value), 2)
        self.system = system

    def convert(self):
        """
        Convert between Metric (cm) and Imperial (inches).
        :return: converted value (rounded to 2 decimals)
        """
        if self.system == "Metric":
            # 1 inch = 2.54 cm
            return round(self.value / 2.54, 2)
        elif self.system == "Imperial":
            return round(self.value * 2.54, 2)
        else:
            raise ValueError("System must be 'Metric' or 'Imperial'.")


class Weight:
    def __init__(self, value: float, system: str):
        """
        Constructor
        :param value: numeric measure (up to two decimals)
        :param system: 'Metric' for kilograms, 'Imperial' for pounds
        """
        self.value = round(float(value), 2)
        self.system = system

    def convert(self):
        """
        Convert between Metric (kg) and Imperial (lb).
        :return: converted value (rounded to 2 decimals)
        """
        if self.system == "Metric":
            # 1 kg = 2.20462 pounds
            return round(self.value * 2.20462, 2)
        elif self.system == "Imperial":
            return round(self.value / 2.20462, 2)
        else:
            raise ValueError("System must be 'Metric' or 'Imperial'.")


class Temperature:
    def __init__(self, value: float, scale: str):
        """
        Constructor
        :param value: numeric temperature (up to two decimals)
        :param scale: 'C', 'F', or 'K'
        """
        self.value = round(float(value), 2)
        self.scale = scale

    def convert(self, target_scale: str):
        """
        Convert temperature between C, F, and K.
        :param target_scale: target scale ('C', 'F', or 'K')
        :return: converted value (rounded to 2 decimals)
        """
        if self.scale == target_scale:
            return self.value

        if self.scale == "C":
            if target_scale == "F":
                return self._c_to_f()
            elif target_scale == "K":
                return self._c_to_k()
        elif self.scale == "F":
            if target_scale == "C":
                return self._f_to_c()
            elif target_scale == "K":
                return self._f_to_k()
        elif self.scale == "K":
            if target_scale == "C":
                return self._k_to_c()
            elif target_scale == "F":
                return self._k_to_f()
        raise ValueError("Invalid temperature scale. Use 'C', 'F', or 'K'.")

    # Specific conversion methods
    def _c_to_f(self):
        return round((self.value * 9/5) + 32, 2)

    def _c_to_k(self):
        return round(self.value + 273.15, 2)

    def _f_to_c(self):
        return round((self.value - 32) * 5/9, 2)

    def _f_to_k(self):
        return round((self.value - 32) * 5/9 + 273.15, 2)

    def _k_to_c(self):
        return round(self.value - 273.15, 2)

    def _k_to_f(self):
        return round((self.value - 273.15) * 9/5 + 32, 2)

# Example usage:
l1 = cm_length = Length(10, "Metric")
print("10 cm in inches:", l1.convert())  

l2 = inch_length = Length(5, "Imperial")
print("5 inches in cm:", l2.convert())  


# Example usage:
w1 = Weight(10, "Metric")
print("10 kg in pounds:", w1.convert())  

w2 = Weight(22.05, "Imperial")
print("22.05 lb in kg:", w2.convert())  

t1 = Temperature(0, "C")
print("0 °C in F:", t1.convert("F"))  
print("0 °C in K:", t1.convert("K"))  

t2 = Temperature(32, "F")
print("32 °F in C:", t2.convert("C")) 






