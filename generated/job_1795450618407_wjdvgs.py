from manim import *


class Main(Scene):
    def construct(self):
        # Sky and ground
        sky = Rectangle(
            width=14.2,
            height=7.2,
            fill_color=BLUE_E,
            fill_opacity=0.22,
            stroke_width=0,
        ).move_to(ORIGIN)
        ground = Rectangle(
            width=14.2,
            height=1.2,
            fill_color=GREEN_E,
            fill_opacity=0.8,
            stroke_width=0,
        ).to_edge(DOWN, buff=0)
        horizon = Line(
            [-7.1, -2.4, 0],
            [7.1, -2.4, 0],
            color=GREEN_A,
            stroke_width=2,
        )

        title = Text("THE WATER CYCLE", font_size=40, weight=BOLD)
        title.to_edge(UP, buff=0.25)

        # Sun
        sun = VGroup(
            Circle(radius=0.42, color=YELLOW, fill_color=YELLOW, fill_opacity=1),
            *[
                Line(
                    0.58 * np.array([np.cos(a), np.sin(a), 0]),
                    0.82 * np.array([np.cos(a), np.sin(a), 0]),
                    color=YELLOW,
                    stroke_width=4,
                )
                for a in np.linspace(0, TAU, 12, endpoint=False)
            ],
        ).move_to([-5.2, 2.25, 0])

        # Ocean and mountains
        ocean = Rectangle(
            width=4.2,
            height=0.55,
            fill_color=BLUE,
            fill_opacity=0.95,
            stroke_color=BLUE_A,
        ).move_to([-4.9, -2.75, 0])

        mountains = VGroup(
            Polygon(
                [-0.2, -2.4, 0],
                [1.2, 0.15, 0],
                [2.5, -2.4, 0],
                color=GREY_B,
                fill_color=GREY_B,
                fill_opacity=1,
            ),
            Polygon(
                [1.1, -2.4, 0],
                [2.7, 0.65, 0],
                [4.5, -2.4, 0],
                color=GREY_A,
                fill_color=GREY_A,
                fill_opacity=1,
            ),
        )

        snow = VGroup(
            Polygon(
                [0.8, -0.58, 0],
                [1.2, 0.15, 0],
                [1.6, -0.58, 0],
                color=WHITE