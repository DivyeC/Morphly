from manim import *

class Main(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-2 * PI, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 1],
            axis_config={"include_tip": True}
        )

        # Labels for the functions
        sine_label = MathTex("y = \\sin(x)").to_edge(UP)
        cosine_label = MathTex("y = \\cos(x)").to_edge(UP)

        # Define the sine wave
        sine_wave = axes.plot(
            lambda x: np.sin(x),
            color=BLUE,
            x_range=[-2 * PI, 2 * PI]
        )

        # Define the cosine wave
        cosine_wave = axes.plot(
            lambda x: np.cos(x),
            color=RED,
            x_range=[-2 * PI, 2 * PI]
        )

        # Animation Sequence
        self.play(Create(axes))
        self.play(Create(sine_wave), Write(sine_label))
        self.wait(1)

        # Morph Sine into Cosine
        self.play(
            Transform(sine_wave, cosine_wave),
            Transform(sine_label, cosine_label),
            run_time=2
        )
        self.wait(2)