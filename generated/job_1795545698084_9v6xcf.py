from manim import *

class Main(Scene):
    def construct(self):
        title = Text("Pythagorean Theorem", font_size=48)
        subtitle = Text("a² + b² = c²", font_size=40, color=YELLOW)
        subtitle.next_to(title, DOWN)
        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))

        a = 3
        b = 4
        scale = 0.8
        origin = LEFT * 2.5 + DOWN * 1.5

        triangle_points = [
            origin,
            origin + RIGHT * a * scale,
            origin + RIGHT * a * scale + UP * b * scale
        ]
        triangle = Polygon(*triangle_points, color=WHITE, fill_opacity=0.2)
        self.play(Create(triangle))

        right_angle = RightAngle(
            Line(triangle_points[0], triangle_points[1]),
            Line(triangle_points[1], triangle_points[2]),
            length=0.3,
            color=WHITE
        )
        self.play(Create(right_angle))

        label_a = Tex("a").next_to(Line(triangle_points[0], triangle_points[1]), DOWN)
        label_b = Tex("b").next_to(Line(triangle_points[1], triangle_points[2]), RIGHT)
        label_c = Tex("c").next_to(Line(triangle_points[0], triangle_points[2]), LEFT, buff=0.1)

        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(1)

        square_a = Square(side_length=a * scale, color=BLUE, fill_opacity=0.4)
        square_a.move_to(triangle_points[0] + RIGHT * a * scale / 2 + DOWN * a * scale / 2)
        self.play(FadeIn(square_a))

        square_b = Square(side_length=b * scale, color=GREEN, fill_opacity=0.4)
        square_b.move_to(triangle_points[1] + UP * b * scale / 2 + RIGHT * b * scale / 2)
        self.play(FadeIn(square_b))

        area_a = Tex(f"a² = {a*a}").scale(0.8).move_to(square_a.get_center())
        area_b = Tex(f"b² = {b*b}").scale(0.8).move_to(square_b.get_center())
        self.play(Write(area_a), Write(area_b))
        self.wait(1)

        hyp_len = (a**2 + b**2) ** 0.5
        square_c = Square(side_length=hyp_len *