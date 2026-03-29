from manim import *

class Main(Scene):
    def construct(self):
        text = TextMobject("jhwdjq", color=YELLOW)
        text.to_edge(UP)

        self.play(Write(text))
        self.wait(1)