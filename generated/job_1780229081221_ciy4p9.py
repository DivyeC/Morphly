from manim import *

class Main(Scene):
    def construct(self):
        title = Text("Chemical Reaction Equation", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        equation_text = Tex(r"$2H_2 + O_2 \rightarrow 2H_2O$", font_size=72)
        reactants_text = Text("Reactants", font_size=36).next_to(equation_text, DOWN, buff=0.5).align_to(equation_text, LEFT)
        products_text = Text("Products", font_size=36).next_to(equation_text, DOWN, buff=0.5).align_to(equation_text, RIGHT)
        arrow_text = Text("Yields / Produces", font_size=24).next_to(equation_text, DOWN, buff=2.5)

        reactants_group = VGroup(equation_text[0:4], reactants_text)
        products_group = VGroup(equation_text[6:], products_text)
        arrow_group = VGroup(equation_text[5], arrow_text)

        self.play(Write(equation_text))
        self.wait(1)

        self.play(
            reactants_group.animate.shift(LEFT * 2),
            products_group.animate.shift(RIGHT * 2)
        )
        self.wait(1)

        self.play(FadeIn(arrow_text, shift=UP))
        self.play(Indicate(equation_text[5], color=YELLOW))
        self.wait(2)

        explanation_reactants = Text("Substances that react together", font_size=24).next_to(reactants_group, DOWN, buff=0.7)
        explanation_products = Text("Substances formed by the reaction", font_size=24).next_to(products_group, DOWN, buff=0.7)

        self.play(Write(explanation_reactants))
        self.wait(1)
        self.play(Write(explanation_products))
        self.wait(2)

        self.play(FadeOut(explanation_reactants), FadeOut(explanation_products))
        self.play(FadeOut(reactants_text), FadeOut(products_text))
        self.play(
            reactants_group.animate.shift(RIGHT * 2),
            products_group.animate.shift(LEFT * 2)
        )