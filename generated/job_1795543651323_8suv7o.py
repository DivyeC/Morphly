from manim import *

class Main(Scene):
    def construct(self):
        circle = Circle(radius=2, color=BLUE)
        circle.set_fill(BLUE, opacity=0.3)
        self.play(Create(circle))
        self.wait(2)