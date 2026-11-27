from manim import *

class Main(Scene):
    def construct(self):
        title = Text("The Solar System", font_size=48).to_edge(UP)
        self.play(Write(title))

        sun = Circle(radius=0.8, fill_color=YELLOW, fill_opacity=1)
        sun_label = Text("Sun", font_size=24).next_to(sun, UP)

        planets_data = [
            ("Mercury", 0.3, TEAL),
            ("Venus", 0.5, ORANGE),
            ("Earth", 0.6, BLUE),
            ("Mars", 0.4, RED),
            ("Jupiter", 1.2, GREY),
            ("Saturn", 1.0, GOLD),
            ("Uranus", 0.7, PURPLE),
            ("Neptune", 0.65, TEAL),
        ]

        planet_groups = VGroup()
        for name, radius, color in planets_data:
            planet = Circle(radius=radius, fill_color=color, fill_opacity=1)
            label = Text(name, font_size=18).next_to(planet, RIGHT)
            group = VGroup(planet, label)
            planet_groups.add(group)

        # Arrange planets in a row with spacing
        planet_groups.arrange(RIGHT, buff=0.3)
        planet_groups.move_to(ORIGIN)

        # Animate sun formation
        self.play(FadeIn(sun), FadeIn(sun_label))

        # Animate planets appearing one by one with slight delays
        for i, group in enumerate(planet_groups):
            self.play(Create(group), run_time=0.4)
            self.wait(0.1)

        self.wait(2)
        self.play(FadeOut(title), FadeOut(sun), FadeOut(sun_label), FadeOut(planet_groups))