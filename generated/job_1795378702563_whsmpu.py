from manim import *
import numpy as np


class Main(Scene):
    def construct(self):
        ray = Arrow(
            start=LEFT * 5.5,
            end=RIGHT * 5.5,
            color=PINK,
            stroke_width=5,
            buff=0,
        )

        wave = ParametricFunction(
            lambda t: np.array([t, 0.65 * np.sin(2 * PI * t / 2.2), 0]),
            t_range=[-5.5, 5.5],
            color=PINK,
            stroke_width=5,
        )

        self.play(Create(ray), run_time=1.5)
        self.play(Create(wave), run_time=2.5)
        self.wait(1)