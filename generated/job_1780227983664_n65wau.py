from manim import *

class Main(Scene):
    def construct(self):
        title = Text("Square Curve vs Cube Curve", font_size=40).to_edge(UP)

        axes = Axes(
            x_range=[-2.2, 2.2, 1],
            y_range=[-8, 8, 2],
            x_length=9,
            y