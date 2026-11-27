from manim import *

class Main(Scene):
    def construct(self):
        # Neural Formulation: "explain the solar system"
        title = Title(r"\textbf{explain the solar system}", font_size=36, color=TEAL)
        self.play(Write(title))
        
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE_C, "stroke_width": 2}
        )
        self.play(Create(axes), run_time=1.5)
        
        graph = axes.plot(lambda x: 0.8 * np.sin(2 * x) + 0.3 * np.cos(3 * x), color=GOLD)
        formula = MathTex(r"\mathcal{F}(\omega) = \int_{-\infty}^\infty f(t) e^{-i\omega t} dt", font_size=36, color=YELLOW)
        formula.to_corner(UR)
        
        self.play(Create(graph), Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=GOLD))
        self.wait(1)
