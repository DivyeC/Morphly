from manim import *

class Main(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=5,
            axis_config={"color": BLUE},
            tips=False,
        )

        x_labels = axes.get_x_axis().add_labels({
            0: MathTex("0"),
            PI / 2: MathTex("\\frac{\\pi}{2}"),
            PI: MathTex("\\pi"),
            3 * PI / 2: MathTex("\\frac{3\\pi}{2}"),
            2 * PI: MathTex("2\\pi"),
        })

        sine_graph = axes.plot(lambda x: np.sin(x), color=YELLOW, x_range=[0, 2 * PI])
        cosine_graph = axes.plot(lambda x: np.cos(x), color=GREEN, x_range=[0, 2 * PI])

        sine_label = MathTex("y = \\sin(x)", color=YELLOW).to_corner(UR)
        cosine_label = MathTex("y = \\cos(x)", color=GREEN).to_corner(UR)

        self.play(Create(axes), run_time=1.5)
        self.play(Create(sine_graph), Write(sine_label), run_time=2)
        self.wait(1)

        self.play(
            Transform(sine_graph, cosine_graph),
            Transform(sine_label, cosine_label),
            run_time=3,
            rate_func=smooth,
        )
        self.wait(2)