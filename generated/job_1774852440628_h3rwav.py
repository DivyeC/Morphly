from manim import *

class Main(Scene):
    def construct(self):
        text = TextMobject("teri maa ka bhossda", color=YELLOW)
        text.to_edge(UP)

        self.play(Write(text))
        self.wait(1)

        text2 = TextMobject("Tu meri maa hai", color=RED)
        text2.next_to(text, DOWN)

        self.play(FadeIn(text2))
        self.play(Create(text.shift(RIGHT * 1.5)), run_time=1)
        self.play(text.animate.shift(RIGHT * 1.5), run_time=1)
        self.play(text.animate.fade_out(), text2.animate.fade_in(), run_time=1)