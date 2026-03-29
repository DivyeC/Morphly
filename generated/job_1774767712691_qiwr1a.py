from manim import *

class Main(Scene):
    def construct(self):
        a, b, c = ValueTracker(3), ValueTracker(4), ValueTracker(5)
        a_value, b_value, c_value = a.get_value(), b.get_value(), c.get_value()

        side_a = Line(ORIGIN, DOWN * a_value)
        side_b = Line(ORIGIN, DOWN * b_value)
        hypotenuse = Line(ORIGIN, DOWN * c_value)

        self.play(Create(side_a), Create(side_b), Create(hypotenuse))

        self.play(a.animate.set_value(3.5), run_time=1)
        self.play(b.animate.set_value(2.4), run_time=1)

        self.play(Create(TextMobject("C"), DOWN * c_value))
        self.play(Create(TextMobject("B"), DOWN * b_value))
        self.play(Create(TextMobject("A"), UP * 0.5))

        self.play(Create(TextMobject("Pythagorean\nTheorem")))

        self.play(Create(TextMobject("A² + B² = C²")))

        self.play(a.animate.set_value(3.5).set_color(RED), run_time=1)
        self.play(b.animate.set_value(2.4).set_color(RED), run_time=1)

        self.play(Create(TextMobject("A² = ")))
        self.play(Create(TextMobject("{:n}²".format(a_value.get_value()))))

        self.play(Create(TextMobject("+ ")))

        self.play(Create(TextMobject("B² = ")))
        self.play(Create(TextMobject("{:n}²".format(b_value.get_value()))))

        self.play(Create(TextMobject("= ")))

        self.play(Create(TextMobject("C² = ")))
        self.play(Create(TextMobject("{:n}²".format(c_value.get_value()))))

        self.play(Create(TextMobject("Therefore, ")))
        self.play(Create(TextMobject("A² + B² = C²"))