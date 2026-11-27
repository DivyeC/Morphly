from manim import *

class Main(Scene):
    def construct(self):
        # Title
        title = Text("The Solar System", font_size=48, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)
        
        # Sun
        sun = Circle(radius=1.3,