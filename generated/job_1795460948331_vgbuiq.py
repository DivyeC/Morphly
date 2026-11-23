from manim import *
import numpy as np

class Main(Scene):
    def construct(self):
        self.camera.background_color = "#10131C"

        title = Text("Square Wave · Fourier Epicycles", font_size=32, color=WHITE)
        title.to_edge(UP, buff=0.35)
        self.add(title)

        # Odd harmonics of the square wave: 4/pi * (sin(x) + sin(3x)/3 + ...)
        harmonics = [1, 3, 5, 7, 9, 11, 13]
        amplitudes = [4 / (PI * n) for n in harmonics]
        radius_scale = 0.80

        chain_center = np.array([-3.15, 0.35, 0.0])
        graph_x0, graph_y0 = 0.15, 0.35
        graph_width, graph_height = 5.55, 2.35
        graph_x1 = graph_x0 + graph_width
        graph_y1 = graph_y0 + graph_height

        graph_axes = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 1],
            x_length=graph_width,
            y_length=graph_height,
            tips=False,
            axis_config={
                "color": GREY_B,
                "stroke_width": 1.5,
                "include_numbers": False,
            },
        ).move_to([graph_x0 + graph_width / 2, graph_y0 + graph_height / 2, 0])

        graph_axes.set_x_axis_label("")
        graph_axes.set_y_axis_label("")
        self.add(graph_axes)

        graph_label = Text("PERIODIC WAVEFORM", font_size=17, color=BLUE_B)
        graph_label.move_to([graph_x0 + graph_width / 2, graph_y1 + 0.37, 0])
        self.add(graph_label)

        def square_wave(x):
            return 1.0 if np.sin(x) >= 0 else -1.0

        def partial_sum(x):
            return sum(
                (4 / (PI * n)) * np.sin(n * x)
                for n in harmonics
            )

        def point_on_graph(x):
            return graph_axes.c2p(x, partial_sum(x))

        trace = TracedPath(
            point_on_graph,
            stroke_color=YELLOW,
            stroke_width=3,
            dissipating_time=0,
        )
        self.add(trace)

        def make_graph_target():
            return ParametricFunction(
                lambda x: graph_axes.c2p(x, partial_sum(x)),
                t_range=[0, 2 * PI],
                color=YELLOW,
                stroke_width=3,