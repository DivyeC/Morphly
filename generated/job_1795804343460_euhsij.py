from manim import *

class Main(Scene):
    def construct(self):
        circle = Circle(radius=2, color=BLUE, fill_opacity=0.5, stroke_width=6)
        self.play(Create(circle), run_time=2)
        self.wait(1)