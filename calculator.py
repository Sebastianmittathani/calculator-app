from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty


class CalculatorScreen(BoxLayout):

    dark = BooleanProperty(True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expression = ""
        self.history = []

    def button_press(self, value):

        if self.ids.display.text == "0" or self.ids.display.text == "Error":
            self.expression = value
        else:
            self.expression += value

        self.ids.display.text = self.expression

    def clear(self):

        self.expression = ""
        self.ids.display.text = "0"

    def backspace(self):

        self.expression = self.expression[:-1]

        if self.expression == "":
            self.ids.display.text = "0"
        else:
            self.ids.display.text = self.expression

    def plus_minus(self):

        if self.expression.startswith("-"):
            self.expression = self.expression[1:]
        else:
            self.expression = "-" + self.expression

        self.ids.display.text = self.expression

    def percentage(self):

        try:
            self.expression = str(float(self.expression) / 100)
            self.ids.display.text = self.expression
        except:
            self.ids.display.text = "Error"

    def calculate(self):

        try:

            answer = str(eval(self.expression))

            self.history.append(
                self.expression + " = " + answer
            )

            self.expression = answer

            self.ids.display.text = answer

        except:

            self.ids.display.text = "Error"

            self.expression = ""

    def show_history(self):

        if len(self.history) == 0:
            self.ids.display.text = "No History"
        else:
            self.ids.display.text = self.history[-1]

    def toggle_theme(self):

        self.dark = not self.dark

        if self.dark:
            self.ids.theme_btn.text = "☀"
        else:
            self.ids.theme_btn.text = "🌙"