from manim import *

class Main(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-2 * PI, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=4,
            axis_config={"include_tip": True},
        )
        x_label = Text("x", font_size=24).next_to(axes.x_axis.get_end(), DR, buff=0.1)
        y_label = Text("y", font_size=24).next_to(axes.y_axis.get_end(), UR, buff=0.1)
        self.add(axes, x_label, y_label)

        phase = ValueTracker(0)
        sine_label = MathTex(r"\sin(x)", font_size=36).to_corner(UR)
        self.add(sine_label)

        def sine_curve():
            return axes.plot(lambda x: np.sin(x + phase.get_value()), color=BLUE, stroke_width=4)

        curve = always_redraw(sine_curve)
        self.add(curve)

        phase.add_updater(lambda m, dt: m.increment_value(dt * 0.8))
        self.wait(2)

        target = PI / 2
        phase.clear_updaters()
        self.play(
            phase.animate.set_value(target),
            run_time=6,
            rate_func=smooth,
        )
        self.wait(1)

        new_label = MathTex(r"\cos(x)", font_size=36).to_corner(UR)
        self.play(Transform(sine_label, new_label))
        self.wait(1)