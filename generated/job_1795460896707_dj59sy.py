from manim import *
import numpy as np


class Main(Scene):
    def construct(self):
        self.camera.background_color = "#080B16"

        title = Tex(r"Riemann zeta: critical strip and non-trivial zeros", font_size=34)
        title.to_edge(UP, buff=0.35)

        plane = ComplexPlane(
            x_range=[-1, 2, 0.5],
            y_range=[-15, 15, 5],
            x_length=7.6,
            y_length=6.1,
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.38,
            },
            axis_config={"stroke_color": GREY_B, "stroke_width": 2},
        )
        plane.shift(DOWN * 0.25)

        x_label = Tex(r"\operatorname{Re}(s)", font_size=25)
        x_label.next_to(plane, DOWN, buff=0.14)
        y_label = Tex(r"\operatorname{Im}(s)", font_size=25)
        y_label.rotate(PI / 2).next_to(plane, LEFT, buff=0.12)

        strip = Polygon(
            plane.c2p(0, -15),
            plane.c2p(1, -15),
            plane.c2p(1, 15),
            plane.c2p(0, 15),
            stroke_width=0,
            fill_color=BLUE_D,
            fill_opacity=0.18,
        )
        critical_line = DashedLine(
            plane.c2p(0.5, -15),
            plane.c2p(0.5, 15),
            dash_length=0.12,
            color=YELLOW,
            stroke_width=3,
        )

        strip_label = Tex(r"0 < \operatorname{Re}(s) < 1", font_size=24)
        strip_label.set_color(BLUE_B)
        strip_label.to_corner(UL, buff=0.3).shift(DOWN * 0.72 + RIGHT * 0.15)

        line_label = Tex(r"\operatorname{Re}(s)=\frac12", font_size=27)
        line_label.set_color(YELLOW)
        line_label.next_to(plane.c2p(0.5, 14), RIGHT, buff=0.12)

        self.play(Write(title), Create(plane), FadeIn(strip), run_time=1.5)
        self.play(Create(critical_line), FadeIn(x_label), FadeIn(y_label))
        self.play(FadeIn(strip_label), FadeIn(line_label))

        # The first several non-trivial zeta zeros lie on the critical line.
        zero_heights = [
            14.134725,