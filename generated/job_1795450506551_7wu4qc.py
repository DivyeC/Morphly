from manim import *

class Main(Scene):
    def construct(self):
        title = Text("Concentric Triangular Waves", font_size=38, weight=BOLD)
        subtitle = Text("Equal waves spreading outward from one center", font_size=22)
        title.to_edge(UP, buff=0.35)
        subtitle.next_to(title, DOWN, buff=0.12)
        self.play(Write(title), FadeIn(subtitle, shift=DOWN * 0.15))

        center = ORIGIN + DOWN * 0.35
        outer_radius = 2.45
        guide = Circle(radius=outer_radius, color=GREY_B, stroke_width=1.5)
        self.play(Create(guide))

        center_dot = Dot(center, color=YELLOW, radius=0.07)
        center_label = Text("source", font_size=18, color=YELLOW)
        center_label.next_to(center_dot, DOWN, buff=0.12)
        self.play(FadeIn(center_dot), FadeIn(center_label))

        colors = [BLUE_B, TEAL_B, GREEN_B, GOLD, ORANGE, RED_B]
        waves = VGroup()
        for index, radius in enumerate([0.58, 1.12, 1.66, 2.20]):
            triangle = RegularPolygon(
                3,
                radius=radius,
                start_angle=PI / 2,
                color=colors[index],
                stroke_width=4,
            )
            triangle.move_to(center)
            waves.add(triangle)

        self.play(
            LaggedStart(
                *[Create(wave) for wave in waves],
                lag_ratio=0.18,
                run_time=2.4,
            )
        )

        wave_label = Text("each outline is a wavefront", font_size=20, color=TEAL_A)
        wave_label.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(wave_label, shift=UP * 0.12))

        explanation = Text(
            "The triangles share a center and grow outward together.",
            font_size=20,
            color=WHITE,
        )
        explanation.next_to(wave_label, UP, buff=0.12)
        self.play(FadeIn(explanation))

        self.wait(1)
        self.play(
            waves.animate.scale(1.08, about_point=center),
            run_time=1.3,
            rate_func=there_and_back,
        )
        self.wait(1)