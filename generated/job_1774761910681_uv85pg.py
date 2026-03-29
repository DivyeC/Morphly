from manim import *

class Main(Scene):
    def construct(self):
        circle = Circle(radius=1, color=YELLOW)
        self.play(Create(circle))