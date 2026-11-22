from manim import *
import numpy as np


class Main(Scene):
    def construct(self):
        center = ORIGIN
        max_radius = 4.2
        wave_count = 7
        period = 2.8
        lifetime = 5.8

        background = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            stroke_width=0,
            fill_color="#071526",
            fill_opacity=1,
        )
        self.add(background)

        source = Dot(center, radius=0.075, color=TEAL_A)
        source_glow = Dot(center, radius=0.19, color=TEAL, fill_opacity=0.16, stroke_width=0)
        self.add(source_glow, source)

        rings = VGroup(
            *[
                Circle(radius=0.1, color=TEAL_A, stroke_width=2.5)
                .move_to(center)
                for _ in range(wave_count)
            ]
        )
        self.add(rings)

        elapsed = ValueTracker(0)

        def update_rings(group):
            time = elapsed.get_value()
            for index, ring in enumerate(group):
                age = time - index * period / wave_count
                if age < 0 or age > lifetime:
                    ring.set_opacity(0)
                    continue

                progress = age / lifetime
                radius = 0.1 + progress * max_radius
                ring.become(
                    Circle(
                        radius=radius,
                        color=TEAL_A,
                        stroke_width=3.0 * (1 - progress) + 0.5,
                    ).move_to(center)
                )
                ring.set_opacity((1 - progress) ** 1.25)

        rings.add_updater(update_rings)
        self.wait(0.5)
        self.play(elapsed.animate.set_value(8.5), run_time=11, rate_func=linear)
        self.wait(1.5)

        rings.clear_updaters()
        self.play(
            rings.animate.set_opacity(0),
            source_glow.animate.set_opacity(0),
            source.animate.set_opacity(0),
            run_time=2.5,
            rate_func=smooth,
        )
        self.wait(2)