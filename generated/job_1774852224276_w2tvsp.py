from manim import *

class Main(Scene):
    def construct(self):
        text = TextMobject("teri maa ka bhossda", color=YELLOW)
        text.to_edge(UP)

        self.play(Write(text))
        self.wait(1)