from manim import *
import numpy as np

class Main(Scene):
    def construct(self):
        # Axes for complex plane
        axes = Axes(
            x_range=[-1, 2, 1],
            y_range=[-2, 30, 5],
            x_length=6,
            y_length=10,
            axis_config={"include_tip": True, "color": GREY_B}
        )
        labels = axes.get_axis_labels(
            Tex("Re(s)").scale(0.8),
            Tex("Im(s)").scale(0.8)
        )
        self.play(Create(axes), FadeIn(labels), run_time=1.5)

        # Critical strip 0 <= Re(s) <= 1
        strip = Rectangle(
            width=axes.x_length / 3,
            height=axes.y_length,
            color=BLUE_E,
            fill_opacity=0.15,
            stroke_width=1
        )
        strip.move_to(axes.c2p(0.5, 14))
        strip_left = axes.get_vertical_line(axes.c2p(0, -2), color=BLUE_D)
        strip_left.set_y(axes.c2p(0, -2)[1], direction=UP)
        strip_left.scale_to_fit_height(axes.y_length)
        strip_left.move_to(axes.c2p(0, 14))

        strip_right = DashedLine(
            axes.c2p(1, -2), axes.c2p(1, 30), color=BLUE_D
        )
        self.play(FadeIn(strip), Create(strip_left), Create(strip_right), run_time=1.5)

        # Critical line Re(s) = 1/2
        crit_line = DashedLine(
            axes.c2p(0.5, -2), axes.c2p(0.5, 30),
            color=YELLOW, stroke_width=2.5, dash_length=0.15
        )
        crit_label = Tex(r"\text{Critical Line } \mathrm{Re}(s)=\tfrac{1}{2}").scale(0.7)
        crit_label.set_color(YELLOW)
        crit_label.next_to(axes.c2p(0.5, 30), UP, buff=0.2)
        self.play(Create(crit_line), Write(crit_label), run_time=1.5)

        # Non-trivial zeros on critical line: imaginary parts
        zeros_im = [14.134725, 21.022040, 25.010858, 30.424876]
        zeros_im = [z for z in zeros_im if z <= 29.5]

        # Mark zeros with glowing spiral vectors
        for im in