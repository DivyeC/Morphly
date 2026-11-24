from manim import *

class Main(Scene):
    def construct(self):
        square = Square()
        self.play(Create(square))
        self.wait()