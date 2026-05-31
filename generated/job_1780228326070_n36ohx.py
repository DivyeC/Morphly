from manim import *

class Main(Scene):
    def construct(self):
        # Define the axes
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 10, 2],
            x_axis_config={"numbers_to_include": [1, 2, 3, 4, 5]},
            y_axis_config={"numbers_to_include": [2, 4, 6, 8, 10]},
            tips=False,
        )

        # Define the exponential function
        def exp_func(x):
            return 2**x

        # Create the exponential curve
        exponential_curve = axes.plot(exp_func, color=BLUE)

        # Add labels for axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")

        # Add title
        title = Tex("Exponential Curve: $y = 2^x$", font_size=48)
        title.to_edge(UP)

        # Add the axes, labels, and curve to the scene
        self.play(Create(axes), Write(x_label), Write(y_label), Write(title))
        self.play(Create(exponential_curve, run_time=3))
        self.wait(2)