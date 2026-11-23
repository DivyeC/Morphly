from manim import *

class Main(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-2 * PI, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=4,
            axis_config={"include_tip": True, "numbers_to_exclude": [0]},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        sine_graph = axes.plot(lambda x: np.sin(x), color=BLUE, x_range=[-2 * PI, 2 * PI])
        cosine_graph = axes.plot(lambda x: np.cos(x), color=RED, x_range=[-2 * PI, 2 * PI])

        sine_label = Tex(r"\sin(x)", color=BLUE).to_corner(UL)
        cosine_label = Tex(r"\cos(x)", color=RED).to_corner(UL)

        self.play(Create(axes), Write(axes_labels))
        self.play(Create(sine_graph), Write(sine_label))
        self.wait(0.5)

        self.play(
            Transform(sine_graph, cosine_graph),
            Transform(sine_label, cosine_label),
            run_time=2,
        )
        self.wait(1)