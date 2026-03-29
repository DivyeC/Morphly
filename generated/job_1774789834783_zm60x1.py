from manim import *

class Main(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=5,
            axis_config={"include_numbers": True, "color": WHITE},
            tips=True,
        )

        sin_label = MathTex(r"y = \sin(x)", color=YELLOW).to_corner(UR)
        cos_label = MathTex(r"y = \cos(x)", color=BLUE).to_corner(UR)

        sin_graph = axes.plot(lambda x: np.sin(x), x_range=[0, 2 * PI], color=YELLOW)
        cos_graph = axes.plot(lambda x: np.cos(x), x_range=[0, 2 * PI], color=BLUE)

        self.play(Create(axes), run_time=1)
        self.play(Create(sin_graph), Write(sin_label), run_time=2)
        self.wait(1)

        self.play(
            Transform(sin_graph, cos_graph),
            Transform(sin_label, cos_label),
            run_time=2,
        )
        self.wait(2)