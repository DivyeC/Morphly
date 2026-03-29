from manim import *

class Main(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-PI, PI, PI/2],
            y_range=[-1.5, 1.5, 1],
            axis_config={"include_tip": True}
        )

        sine_func = axes.plot(lambda x: np.sin(x), color=BLUE)
        sine_label = MathTex("y = \\sin(x)").to_edge(UP).set_color(BLUE)

        cosine_func = axes.plot(lambda x: np.cos(x), color=RED)
        cosine_label = MathTex("y = \\cos(x)").to_edge(UP).set_color(RED)

        self.play(Create(axes), Create(sine_func))
        self.play(Write(sine_label))
        self.wait(1)

        self.play(
            ReplacementTransform(sine_func, cosine_func),
            ReplacementTransform(sine_label, cosine_label),
            run_time=2
        )
        self.wait(2)