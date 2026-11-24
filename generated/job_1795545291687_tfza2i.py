from manim import *

class Main(Scene):
    def construct(self):
        triangle = Triangle()
        self.play(Create(triangle))
        self.wait(2)