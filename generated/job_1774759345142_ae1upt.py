from manim import *

class Main(Scene):
    def construct(self):
        a, b, c = ValueTracker(3, 4, 5)
        side_a = NumberLine(x_range=[0, 6], length=7, numbers_to_include=None)
        side_b = NumberLine(x_range=[0, 6], length=7, numbers_to_include=None)
        point_c = Dot(origin=(3, 0))

        self.play(Create(side_a), Create(side_b))
        self.play(Create(point_c))

        self.play(Write(side_a.get_text(a.get_value()), x=side_a.get_x(a.get_value())), run_time=1)
        self.play(Write(side_b.get_text(b.get_value()), x=side_b.get_x(b.get_value())), run_time=1)

        self.play(a.animate.set_value(a.get_value() + 1), run_time=1)
        self.play(Create(line = Line(point_c.get_center(), side_a.number_to_point(a.get_value()))))

        self.play(Write(side_a.get_text(a.get_value() + 1), x=side_a.get_x(a.get_value() + 1), run_time=1) )
        self.play(Create(point_d = Dot(side_a.number_to_point(a.get_value() + 1))))

        self.play(b.animate.set_value(b.get_value() - 1.4142), run_time=1)
        self.play(Create(line = Line(point_c.get_center(), side_b.number_to_point(b.get_value()))))

        self.play(Write(side_b.get_text(b.get_value()), x=side_b.get_x(b.get_value()), run_time=1))
        self.play(Create(point_e = Dot(side_b.number_to_point(b.get_value()))))

        self.play(Create(triangle = Polygon(point_c.get_center(), point_d.get_position(), point_e.get_position())))

        self.play(Write(Text