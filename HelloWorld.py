# coding: utf-8

__Author__ = "Gabriely Da Mata Batista"
__Author2__ = "Bruno Sevalho Wesen"

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
# from kivy.utils import get_color_from_hex


class Tela1(FloatLayout):
    def imprimir(self):
        texto = self.ids.text_input
        print(texto.text)


class HelloWorld(App):
    def build(self):
        return Tela1()


if __name__ == "__main__":
    janela = HelloWorld()
    janela.title = "Primeiro Programa"
    janela.run()
