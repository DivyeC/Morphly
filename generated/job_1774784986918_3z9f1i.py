from manim import *

class Main(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-PI, PI, PI/2],
            y_range=[-1.5, 1.5, 1],
            x_length=6,
            y_length=3,
            axis_config={"include_numbers": True},
            tips=False,
        )

        # Create the sine wave function
        def func(x):
            return np.sin(x)

        # Create the sine wave graph
        sin_wave = axes.plot(func, color=BLUE)

        # Display the axes and the sine wave
        self.play(Create(axes), Create(sin_wave))
        self.wait(2)