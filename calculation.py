class Calculation:

    def __init__(self, calc: str, res: str):
        self.__calc = calc
        self.__res = res

    def get_calculation(self) -> str:
        return self.__calc

    def set_calculation(self, calc: str):
        self.__calc = calc

    def get_result(self) -> str:
        return self.__res

    def set_result(self, res: str):
        self.__res = res

    calculation = property(fget=get_calculation, fset=set_calculation)
    result = property(fget=get_result, fset=set_result)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.calculation == other.calculation

    def __str__(self):
        return str(self.__dict__)

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            raise NotImplementedError("Comparison with non-Calculation object is not supported.")
        return self.calculation < other.calculation

    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            raise NotImplementedError("Comparison with non-Calculation object is not supported.")
        return self.calculation > other.calculation
