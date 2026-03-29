from manim import *

class Main(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-PI, PI, PI/2],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            y_length=4,
            axis_config={"include_tip": True}
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        sine_wave = axes.plot(lambda x: np.sin(x), color=BLUE)
        sine_label = MathTex("y = \\sin(x)", color=BLUE).next_to(axes, UP)

        cosine_wave = axes.plot(lambda x: np.cos(x), color=RED)
        cosine_label = MathTex("y = \\cos(x)", color=RED).next_to(axes, UP)

        self.play(Create(axes), Write(labels))
        self.play(Create(sine_wave), Write(sine_label))
        self.wait(1)

        self.play(
            ReplacementTransform(sine_wave, cosine_wave),
            ReplacementTransform(sine_label, cosine_label),
            run_time=2
        )
        self.wait(2)