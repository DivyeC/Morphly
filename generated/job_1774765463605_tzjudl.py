from manim import *

class Main(Scene):
    def construct(self):
        square = Square(side_length=3)
        self.play(Create(square))