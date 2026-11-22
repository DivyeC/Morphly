from manim import *

class Main(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-2 * PI, 2 * PI, PI],
            y_range=[-1.5, 1.5, 0.5],
            x_length=11,
            y_length=4.5,
            axis_config={"include_numbers": False},
            tips=False,
        )
        axes.to_edge(DOWN, buff=0.7)

        x_label = MathTex("x").next_to(axes.x_axis.get_end(), RIGHT, buff=0.15)
        y_label = MathTex("y").next_to(axes.y_axis.get_end(), UP, buff=0.15)

        sine = axes.plot(lambda x: np.sin(x), x_range=[-2 * PI, 2 * PI], color=BLUE, stroke_width=4)
        cosine = axes.plot(lambda x: np.cos(x), x_range=[-2 * PI, 2 * PI], color=ORANGE, stroke_width=4)

        title = MathTex(r"y=\sin(x)", color=BLUE).to_edge(UP, buff=0.5)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(sine), Write(title))
        self.wait(0.5)

        cosine_title = MathTex(r"y=\cos(x)", color=ORANGE).to_edge(UP, buff=0.5)
        self.play(
            Transform(sine, cosine),
            Transform(title, cosine_title),
            run_time=2.5,
            rate_func=smooth,
        )
        self.wait(1)