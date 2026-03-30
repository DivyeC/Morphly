from manim import *

class Main(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-PI, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 1],
            axis_config={"include_tip": True}
        )
        
        # Labels for the functions
        sine_label = MathTex("y = \\sin(x)").to_edge(UP)
        cosine_label = MathTex("y = \\cos(x)").to_edge(UP)

        # Definitions of functions
        sine_graph = axes.plot(lambda x: np.sin(x), color=BLUE, x_range=[-PI, 2 * PI])
        cosine_graph = axes.plot(lambda x: np.cos(x), color=RED, x_range=[-PI, 2 * PI])

        # Initial Setup
        self.play(Create(axes))
        self.play(Create(sine_graph), Write(sine_label))
        self.wait(1)

        # Morphing animation
        self.play(
            Transform(sine_graph, cosine_graph),
            ReplacementTransform(sine_label, cosine_label),
            run_time=2
        )
        
        self.wait(2)

        # Highlight the phase shift property
        shift_text = Text("Shift of π/2", font_size=24).next_to(sine_label, DOWN)
        self.play(Write(shift_text))
        
        # Return to Sine to show periodicity
        self.play(
            Transform(sine_graph, axes.plot(lambda x: np.sin(x), color=BLUE, x_range=[-PI, 2 * PI])),
            ReplacementTransform(cosine_label, sine_label),
            FadeOut(shift_text),
            run_time=2
        )
        
        self.wait(1)