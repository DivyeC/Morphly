from manim import *

class Main(Scene):
    def construct(self):
        self.camera.background_color = "#EAF7FF"

        title = Text("The Water Cycle", font_size=42, color="#14324A", weight=BOLD)
        title.to_edge(UP, buff=0.35)

        ocean = Rectangle(
            width=3.2, height=1.0, fill_color="#3D9BE9", fill_opacity=0.9,
            stroke_color="#2476B7"
        ).move_to(LEFT * 4.2 + DOWN * 2.25)
        ocean_label = Text("Ocean", font_size=25, color=WHITE).move_to(ocean)

        ground = Line(LEFT * 1.0 + DOWN * 1.75, RIGHT * 5.9 + DOWN * 1.75, color="#537B39", stroke_width=6)
        hill = Polygon(
            RIGHT * 0.5 + DOWN * 1.75,
            RIGHT * 2.8 + UP * 0.35,
            RIGHT * 4.8 + DOWN * 1.75,
            fill_color="#83B85A", fill_opacity=1,
            stroke_color="#537B39"
        )
        hill_label = Text("Land", font_size=23, color="#25451E").move_to(RIGHT * 3.0 + DOWN * 1.35)

        sun = Circle(radius=0.48, fill_color="#FFD34E", fill_opacity=1, stroke_color="#F0A928")
        sun.move_to(RIGHT * 4.9 + UP * 2.6)
        sun_label = Text("Sun", font_size=22, color="#6B4D00").next_to(sun, DOWN, buff=0.12)

        cloud = VGroup(
            Circle(radius=0.38, fill_color=WHITE, fill_opacity=1, stroke_color="#8CA9B8"),
            Circle(radius=0.52, fill_color=WHITE, fill_opacity=1, stroke_color="#8CA9B8").shift(LEFT * 0.42 + UP * 0.05),
            Circle(radius=0.43, fill_color=WHITE, fill_opacity=1, stroke_color="#8CA9B8").shift(RIGHT * 0.42 + UP * 0.02),
            Rectangle(width=1.25, height=0.38, fill_color=WHITE, fill_opacity=1, stroke_color="#8CA9B8").shift(DOWN * 0.18)
        ).move_to(UP * 1.45 + RIGHT * 0.55)
        cloud_label = Text("Clouds", font_size=22, color="#28495C").next_to(cloud, UP