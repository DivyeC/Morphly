from manim import *

class Main(Scene):
    def construct(self):
        title = Text("Pythagorean Theorem", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))

        # Right triangle
        A = LEFT * 3 + DOWN * 2
        B = RIGHT * 2 + DOWN * 2
        C = LEFT * 3 + UP * 1

        triangle = Polygon(A, B, C, color=BLUE, fill_opacity=0.3, stroke_width=3)
        self.play(Create(triangle))

        right_angle = RightAngle(
            Line(B, A), Line(B, C), length=0.4, quadrant=(1, 1)
        )
        self.play(Create(right_angle))

        # Side labels
        a_label = MathTex("a").next_to(Line(B, C), RIGHT)
        b_label = MathTex("b").next_to(Line(A, B), DOWN)
        c_label = MathTex("c").next_to(Line(A, C), LEFT)

        self.play(Write(a_label), Write(b_label), Write(c_label))
        self.wait(0.5)

        formula = MathTex("a^2 + b^2 = c^2", font_size=56)
        formula.next_to(triangle, RIGHT * 2)
        self.play(Write(formula))
        self.wait(1)

        self.play(Circumscribe(formula, color=YELLOW))
        self.wait(1)

        # Show squares on sides visually
        self.play(Indicate(a_label, color=GREEN), Indicate(b_label, color=GREEN),
                  Indicate(c_label, color=GREEN))
        self.wait(1)

        final_text = Text("The square of the hypotenuse equals\nthe sum of the squares of the legs",
                          font_size=28)
        final_text.next_to(formula, DOWN, buff=0.8)
        self.play(FadeIn(final_text))
        self.wait(2)