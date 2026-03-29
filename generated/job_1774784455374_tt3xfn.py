from manim import *

class Main(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-PI, PI, PI/2],
            y_range=[-1.5, 1.5, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True}
        )

        sin_wave = axes.plot(
            lambda x: np.sin(x),
            color=BLUE,
            x_range=[-PI, PI]
        )

        self.play(Create(axes))
        self.play(Create(sin_wave))
        self.wait(2)