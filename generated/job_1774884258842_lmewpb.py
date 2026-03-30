from manim import *

class Main(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1.5, 1.5, 1],
            axis_config={"color": BLUE}
        )

        sine_graph = axes.plot(lambda x: np.sin(x), color=YELLOW)
        cosine_graph = axes.plot(lambda x: np.cos(x), color=WHITE)

        sine_label = MathTex("y = \\sin(x)").set_color(YELLOW).next_to(sine_graph, UP)
        cosine_label = MathTex("y = \\cos(x)").set_color(WHITE).next_to(cosine_graph, UP)

        self.play(Create(axes))
        self.play(Create(sine_graph), Write(sine_label))
        self.wait(1)

        self.play(
            ReplacementTransform(sine_graph, cosine_graph),
            ReplacementTransform(sine_label, cosine_label),
            run_time=2
        )
        self.wait(2)