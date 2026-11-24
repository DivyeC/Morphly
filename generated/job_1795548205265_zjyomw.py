from manim import *

class Main(Scene):
    def construct(self):
        title = Title(r"Unit Circle \& Harmonic Projection", font_size=38, color=TEAL)
        self.play(Write(title))
        
        axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            axis_config={"color": GREY_B}
        )
        circle = Circle(radius=1.8, color=BLUE).move_to(axes.c2p(0, 0))
        self.play(Create(axes), Create(circle), run_time=1.5)
        
        dot = Dot(color=YELLOW).move_to(circle.point_at_angle(0))
        line_cos = Line(axes.c2p(0, 0), axes.c2p(1.8, 0), color=RED)
        
        self.play(FadeIn(dot), Create(line_cos))
        self.play(Rotate(dot, angle=2*PI, about_point=axes.c2p(0, 0)), run_time=3.0)
        self.wait(1)
