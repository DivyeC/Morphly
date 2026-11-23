from manim import *

class Main(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-2 * PI, 2 * PI, PI],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            y_length=4,
            axis_config={"include_tip": False},
        )
        x_labels = axes.get_x_axis_label(Tex(r"x"))
        y_labels = axes.get_y_axis_label(Tex(r"y"))
        self.play(Create(axes), Write(x_labels), Write(y_labels))

        sine_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        sine_label = Tex(r"\sin(x)", color=BLUE).next_to(axes.c2p(PI / 2, 1), UP)
        self.play(Create(sine_graph), Write(sine_label))

        cosine_graph = axes.plot(lambda x: np.cos(x), color=YELLOW)
        cosine_label = Tex(r"\cos(x)", color=YELLOW).next_to(axes.c2p(0, 1), UR)

        self.play(
            Transform(sine_graph, cosine_graph),
            Transform(sine_label, cosine_label),
            run_time=3,
        )
        self.wait()