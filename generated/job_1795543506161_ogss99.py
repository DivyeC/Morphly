from manim import *
import numpy as np


class Main(Scene):
    def construct(self):
        self.camera.background_color = "#10131C"

        title = Text("Square Wave from Rotating Epicycles", font_size=34)
        title.to_edge(UP, buff=0.35)
        self.add(title)

        # Fourier series: a square wave formed by odd harmonics.
        harmonics = [1, 3, 5, 7, 9]
        amplitudes = [2.0 / (np.pi * n) for n in harmonics]
        colors = [BLUE_B, TEAL_B, GREEN_B, YELLOW_B, ORANGE]

        center = LEFT * 3.35 + DOWN * 0.1
        scale = 1.25
        time_value = ValueTracker(0.0)

        def chain_points(t):
            points = [center]
            endpoint = center.copy()
            for n, amplitude in zip(harmonics, amplitudes):
                angle = -n * t
                endpoint = endpoint + scale * amplitude * np.array(
                    [np.cos(angle), np.sin(angle), 0.0]
                )
                points.append(endpoint.copy())
            return points

        circles = VGroup()
        vectors = VGroup()
        for i, (n, amplitude, color) in enumerate(zip(harmonics, amplitudes, colors)):
            def make_circle(index, harmonic, amp, col):
                circle = Circle(radius=scale * amp, color=col, stroke_width=1.5)
                circle.set_stroke(opacity=0.38)
                circle.add_updater(
                    lambda mob, dt, idx=index, h=harmonic, a=amp:
                    mob.move_to(chain_points(time_value.get_value())[idx])
                )
                return circle

            circle = make_circle(i, n, amplitude, color)
            circles.add(circle)

            vector = Line(ORIGIN, RIGHT, color=color, stroke_width=3)
            vector.add_updater(
                lambda mob, dt, idx=i:
                mob.put_start_and_end_on(
                    chain_points(time_value.get_value())[idx],
                    chain_points(time_value.get_value())[idx + 1],
                )
            )
            vectors.add(vector)

        endpoint_dot = Dot(radius=0.055, color=WHITE)
        endpoint_dot.add_updater(
            lambda mob: mob.move_to(chain_points(time_value.get_value())[-1])
        )

        axes = Axes(
            x_range=[0, TAU, PI / 2],
            y_range=[-1.35, 1.35, 0.5],
            x_length=5.7,
            y_length=3.8,
            axis_config={"color": GREY_B, "stroke_width": 1.5},
            x_axis_config={"numbers_to_exclude": [