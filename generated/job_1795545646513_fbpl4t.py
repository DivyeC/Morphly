from manim import *

class Main(Scene):
    def construct(self):
        title = Text("Pythagoras' Theorem", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        equation = MathTex("a^2 + b^2 = c^2", font_size=60)
        equation.next_to(title, DOWN, buff=0.8)
        self.play(Write(equation))
        self.wait(0.5)

        triangle = Polygon(
            ORIGIN,
            RIGHT * 3,
            RIGHT * 3 + UP * 4,
            color=WHITE,
            fill_opacity=0.1,
        )
        triangle.scale(0.8)
        triangle.shift(DOWN * 1.5)
        self.play(Create(triangle))

        a_label = MathTex("a").next_to(
            Line(triangle.get_corner(DL), triangle.get_corner(DR)), DOWN, buff=0.2
        )
        b_label = MathTex("b").next_to(
            Line(triangle.get_corner(DR), triangle.get_corner(UR)), RIGHT, buff=0.2
        )
        c_label = MathTex("c").next_to(
            Line(triangle.get_corner(DL), triangle.get_corner(UR)), UL, buff=0.1
        )

        self.play(Write(a_label), Write(b_label), Write(c_label))
        self.wait(0.5)

        right_angle = RightAngle(
            Line(triangle.get_corner(DR), triangle.get_corner(DL)),
            Line(triangle.get_corner(DR), triangle.get_corner(UR)),
            length=0.4,
        )
        self.play(Create(right_angle))
        self.wait(0.5)

        sq_a = Square(side_length=3 * 0.8, color=BLUE, fill_opacity=0.3)
        sq_a.next_to(Line(triangle.get_corner(DL), triangle.get_corner(DR)), DOWN, buff=0)
        sq_a.align_to(triangle.get_corner(DL), LEFT)

        sq_b = Square(side_length=4 * 0.8, color=GREEN, fill_opacity=0.3)
        sq_b.next_to(Line(triangle.get_corner(DR), triangle.get_corner(UR)), RIGHT, buff=0)
        sq_b.align_to(triangle.get_corner(DR), DOWN)

        self.play(FadeIn(sq_a), FadeIn(sq_b))
        self.wait(0.5)

        label_a_sq = MathTex("a^2").move_to(sq_a.get_center())
        label_b