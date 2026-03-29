from manim import *

class Main(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-4 * PI / 3, 4 * PI / 3, PI / 2],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=5,
            axis_config={"color": BLUE_D, "include_numbers": False},
            tips=True,
        )

        x_labels = axes.get_x_axis().add_labels({
            -PI: MathTex("-\\pi"),
            -PI/2: MathTex("-\\frac{\\pi}{2}"),
            PI/2: MathTex("\\frac{\\pi}{2}"),
            PI: MathTex("\\pi"),
        })

        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        sine_label = MathTex("y = \\sin(x)", color=YELLOW).to_corner(UR).shift(DOWN * 0.5)
        cosine_label = MathTex("y = \\cos(x)", color=GREEN).to_corner(UR).shift(DOWN * 0.5)

        sine_curve = axes.plot(lambda x: np.sin(x), color=YELLOW, x_range=[-4 * PI / 3, 4 * PI / 3])
        cosine_curve = axes.plot(lambda x: np.cos(x), color=GREEN, x_range=[-4 * PI / 3, 4 * PI / 3])

        title = Text("Sine Wave Morphing into Cosine Wave", font_size=36).to_edge(UP)

        self.play(Write(title), run_time=1)
        self.play(Create(axes), Write(axes_labels), run_time=1.5)
        self.play(Create(sine_curve), Write(sine_label), run_time=2)
        self.wait(1)

        # Morph sine into cosine
        self.play(
            Transform(sine_curve, cosine_curve),
            Transform(sine_label, cosine_label),
            run_time=3,
            rate_func=smooth,
        )
        self.wait(2)