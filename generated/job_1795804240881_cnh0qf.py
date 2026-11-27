from manim import *

class Main(Scene):
    def construct(self):
        # Title
        title = Text("The Solar System", font_size=48, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        # Sun with glow
        sun = Circle(radius=0.5, color=YELLOW, fill_opacity=1)
        sun_glow = Circle(radius=0.75, color=YELLOW, fill_opacity=0.3)
        sun_group = VGroup(sun_glow, sun)
        sun_label = Text("Sun", font_size=24, color=YELLOW).next_to(sun, DOWN, buff=0.2)
        self.play(FadeIn