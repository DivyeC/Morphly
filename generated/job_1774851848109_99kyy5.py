from manim import *

class Main(Scene):
    def construct(self):
        class Earth(Sphere):
            def __init__(self, radius=1, color=YELLOW, **kwargs):
                super().__init__(radius=radius, color=color, **kwargs)

        class SinWave(VMobject):
            def __init__(self, length=10, amplitude=1, **kwargs):
                points = [
                    self.to_point(self.get_point(t)) for t in np.linspace(0, 2 * np.pi, 100)
                ]
                self.set_points_smoothly(points)
                self.set_color(RED)
                self.set_stroke(width=2)
                self.set_amplitude(amplitude)

                self.angle = 0

            def get_point(self, t):
                return self.amplitude * np.sin(t)

            def set_amplitude(self, amplitude):
                self.function = lambda t: self.amplitude * np.sin(t)

        earth = Earth()
        sin_wave = SinWave()

        self.play(Create(earth), Create(sin_wave))

        self.play(Animate(earth.rotate, around_z_axis=sin_wave.function), run_time=10)

        self.wait(2)