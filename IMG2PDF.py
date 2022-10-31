from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition
import img2pdf


Window.clearcolor = '#a9a9a9'


class front_screen(Screen):
    def next_screen(self, *args):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = self.manager.next()


class FILECHOOSER(Screen):

    def __init__(self, **kwargs):
        super(FILECHOOSER, self).__init__(**kwargs)
        self.path = None
        self.filename = None

    def selected(self, *args):
        self.path = [args[1]]

    def converter(self):
        filename = self.manager.get_screen('textinput')
        self.filename = filename.ids.Input.text
        file = open(f'{self.filename}.pdf', 'wb')
        pdf_doc = img2pdf.convert(self.path[0])
        file.write(pdf_doc)
        file.close()

    def prev_screen(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = self.manager.previous()

    def next_screen(self, *args):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = self.manager.next()


class Text_Input(Screen):

    def __getattr__(self, item):
        FILECHOOSER.converter(item)

    def prev_screen(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = self.manager.previous()

    def next_screen(self, *args):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = self.manager.next()


class IMG2PDF(App):
    def build(self):
        arrange_screen = ScreenManager()
        arrange_screen.add_widget(front_screen(name='Menu'))
        arrange_screen.add_widget(Text_Input(name='textinput'))
        arrange_screen.add_widget(FILECHOOSER(name='filechooser'))
        return arrange_screen


if __name__ == '__main__':
    IMG2PDF().run()
