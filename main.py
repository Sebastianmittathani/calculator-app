from kivy.app import App
from calculator import CalculatorScreen

class CalculatorApp(App):
    def build(self):
        self.title = "Calculator"
        return CalculatorScreen()

CalculatorApp().run()