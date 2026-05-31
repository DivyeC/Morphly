from manim import *

class Main(Scene):
    def construct(self):
        title = Text("Square Curve vs Cube Curve", font_size=40).to_edge(UP)

        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-9, 9, 3],
            x_length=9,
            y_length=5.5,
            axis_config={"include_numbers": True},
            tips=True,
        ).shift(DOWN * 0.3)

        x_label = axes.get_x_axis_label(Text("x", font_size=24))
        y_label = axes.get_y_axis_label(Text("y", font_size=24))

        square_curve = axes.plot(
            lambda x: x**2,
            x_range=[-3, 3],
            color=BLUE,
            stroke_width=5,
        )

        cube_curve = axes.plot(
            lambda x: x**3,
            x_range=[-2.08, 2.08],
            color=RED,
            stroke_width=5,
        )

        square_label = MathTex("y=x^2", color=BLUE, font_size=36)
        square_label.next_to(axes.c2p(2.1, 4.41), RIGHT)

        cube_label = MathTex("y=x^3", color=RED, font_size=36)
        cube_label.next_to(axes.c2p(1.45, 3.05), RIGHT)

        legend_box = VGroup(
            VGroup(Line(LEFT * 0.4, RIGHT * 0.4, color=BLUE, stroke_width=5), MathTex("y=x^2", font_size=30)).arrange(RIGHT, buff=0.2),
            VGroup(Line(LEFT * 0.4, RIGHT * 0.4, color=RED, stroke_width=5), MathTex("y=x^3", font_size=30)).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        legend_box.to_corner(UR).shift(DOWN * 0.8)

        square_note = Text("Square curve: always nonnegative", font_size=24, color=BLUE)
        cube_note = Text("Cube curve: negative on the left, positive on the right", font_size=24, color=RED)
        notes = VGroup