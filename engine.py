class CalculatorEngine:

    @staticmethod
    def solve(expression):

        try:
            return str(eval(expression))

        except:
            return "Error"