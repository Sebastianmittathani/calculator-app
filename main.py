from kivy.app import App
from calculator import CalculatorScreen

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class CalculatorScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1

        self.display = TextInput(
            text="",
            multiline=False,
            readonly=True,
            halign="right",
            font_size=40
        )

        self.add_widget(self.display)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C"]
        ]

        for row in buttons:

            row_layout = GridLayout(cols=len(row))

            for label in row:

                button = Button(
                    text=label,
                    font_size=30
                )

                button.bind(on_press=self.button_press)

                row_layout.add_widget(button)

            self.add_widget(row_layout)

    def button_press(self, instance):

        text = instance.text

        if text == "C":
            self.display.text = ""

        elif text == "=":

            try:
                self.display.text = str(eval(self.display.text))
            except:
                self.display.text = "Error"

        else:
            self.display.text += text


class CalculatorApp(App):

    def build(self):

        self.title = "Calculator"

        return CalculatorScreen()


if __name__ == "__main__":
    CalculatorApp().run()