from manim import *

class Main(Scene):
    def construct(self):
        title = Text("Turn sine into cosine", font_size=36)
        title.to_edge(UP)

        axes = Axes(
            x_range=[-2 * PI, 2 * PI, PI],
            y_range=[-1.5, 1.5, 1],
            x_length=11,
            y_length=4.5,
            axis_config={"include_numbers": False},
            tips=False,
        )
        axes_labels = axes.get_axis_labels(
            Tex("x"), Tex("y")
        )

        sine = axes.plot(lambda x: np.sin(x), color=BLUE, stroke_width=4)
        sine_label = Tex(r"y=\sin x", color=BLUE, font_size=34)
        sine_label.to_corner(UR).shift(DOWN * 0.8)

        self.play(Write(title), Create(axes), Write(axes_labels))
        self.play(Create(sine), FadeIn(sine_label))
        self.wait(0.7)

        cosine = axes.plot(lambda x: np.cos(x), color=YELLOW, stroke_width=4)
        cosine_label = Tex(r"y=\cos x", color=YELLOW, font_size=34)
        cosine_label.move_to(sine_label)

        shift_note = Tex(r"\sin(x+\frac{\pi}{2})=\cos x", font_size=32)
        shift_note.to_edge(DOWN)

        self.play(
            Transform(sine, cosine),
            Transform(sine_label, cosine_label),
            FadeIn(shift_note, shift=UP * 0.2),
            run_time=2.5,
        )
        self.wait(2)