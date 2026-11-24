from manim import *

class Main(Scene):
    def construct(self):
        triangle = Triangle()
        triangle.set_fill(BLUE, opacity=0.5)
        triangle.set_stroke(YELLOW, width=4)

        self.play(Create(triangle))
        self.play(triangle.animate.rotate(PI / 2))
        self.wait(2)