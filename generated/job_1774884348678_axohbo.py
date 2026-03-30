from manim import *

class Main(Scene):
    def construct(self):
        title = Text("Wave Interference", font_size=40, color=YELLOW).to_edge(UP, buff=0.3)
        self.play(Write(title))

        # Labels
        label1 = Text("Wave 1", font_size=24, color=BLUE).move_to(UP * 2.5 + LEFT * 5)
        label2 = Text("Wave 2", font_size=24, color=RED).move_to(UP * 0.5 + LEFT * 5)
        label3 = Text("Superposition", font_size=24, color=GREEN).move_to(DOWN * 1.5 + LEFT * 5)

        # Axes for each wave
        ax1 = Axes(x_range=[0, 4 * PI, 0.1], y_range=[-1.5, 1.5, 0.5],
                    x_length=9, y_length=1.5,
                    axis_config={"include_ticks": False}).move_to(UP * 2)
        ax2 = Axes(x_range=[0, 4 * PI, 0.1], y_range=[-1.5, 1.5, 0.5],
                    x_length=9, y_length=1.5,
                    axis_config={"include_ticks": False}).move_to(ORIGIN)
        ax3 = Axes(x_range=[0, 4 * PI, 0.1], y_range=[-2.5, 2.5, 0.5],
                    x_length=9, y_length=2,
                    axis_config={"include_ticks": False}).move_to(DOWN * 2)

        self.play(Create(ax1), Create(ax2), Create(ax3),
                  Write(label1), Write(label2), Write(label3), run_time=1.5)

        phase_shift = ValueTracker(0)

        wave1 = always_redraw(lambda: ax1.plot(
            lambda x: np.sin(x), x_range=[0, 4 * PI], color=BLUE, stroke_width=3
        ))

        wave2 = always_redraw(lambda: ax2.plot(
            lambda x: np.sin(x + phase_shift.get_value()), x_range=[