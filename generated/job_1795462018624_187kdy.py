from manim import *

class Main(Scene):
    def construct(self):
        # your animation for: "draw a circle"
        circle = Circle(color=BLUE, stroke_width=6)
        self.play(Create(circle))
        self.wait(1)