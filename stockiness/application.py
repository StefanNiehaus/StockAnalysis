from kivy.app import App
from kivy.uix.button import Button


class StockMarketApp(App):
    def build(self):
        return Button(text='Hello World', pos=(20, 350), size_hint=(.25, .18))


if __name__ == '__main__':
    StockMarketApp().run()
