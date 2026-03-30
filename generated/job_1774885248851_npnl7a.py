from manim import *

class Main(Scene):
    def construct(self):
        text_sequence = VGroup(*[Text(r"baa", color=YELLOW) for _ in range(3)] +
                              [Text(r"abaa", color=BLUE) for _ in range(2)] +
                              [Text(r"baaa", color=YELLOW) for _ in range(3)])

        self.play(Write(text_sequence))
        self.wait(1)
        self.play(FadeOut(text_sequence))