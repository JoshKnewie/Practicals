from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class ConvertDistance(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('converter.kv')
        return self.root

    def handle_calculate(self):
         value = self.error_handling()
         result = value * 1.60934
         self.root.ids.output_number.text = str(result)

    def plus_minus_one(self, modifier):
        value = self.error_handling()
        result = value + modifier
        self.root.ids.input_number.text = str(result)
        self.handle_calculate()

    def error_handling(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except:
            return 0

ConvertDistance().run()