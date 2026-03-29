from manim import *

class Main(Scene):
    def construct(self):
        x_range = NumberLine(x_min=-10, x_max=10, unit_size=1)
        x = ValueTracker(0)

        sine_function = Function(lambda x: np.sin(x), x_min=-10, x_max=10)

        graph = GraphOfFunction(sine_function, x_min=-10, x_max=10, color=YELLOW)

        self.play(Create(x_range), Create(x), Create(graph))

        self.play(x.animate.set_value, 2*PI, run_time=4)
        self.wait(2)