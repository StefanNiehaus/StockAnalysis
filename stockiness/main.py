from kivy.app import App
from kivy.logger import Logger
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


class SingleViewSectionController(Widget):
    pass


class MultiViewSectionController(Widget):
    pass


class NavigationController(BoxLayout):

    def single_view_section(self):
        Logger.info('I have clicked the single_view_section')

    def multi_view_section(self):
        Logger.info('I have clicked the multi_view_section')


class RootController(FloatLayout):
    """Create a controller that receives a custom widget from the kv lang file.

    Add an action to be called from the kv lang file.
    """
    navigation = NavigationController()
    title = ObjectProperty()
    info = StringProperty()

    def do_action(self):
        Logger.info('Logged')


class StockApp(App):
    def build(self):
        return RootController(info="hello")


if __name__ == '__main__':
    StockApp().run()
