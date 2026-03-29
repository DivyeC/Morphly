from manim import *

class Main(Scene):
    def construct(self):
        cat = Circle(radius=0.2, fill_opacity=1, color=YELLOW)
        cat.shift(RIGHT * 2 + UP * 1.5)

        milk = Rectangle(height=1, width=3, fill_opacity=1, color=BLUE)
        milk.shift(RIGHT * 3.5 + UP * 1.5)

        cup = Circle(radius=0.1, fill_opacity=1, color=GREY)
        cup.shift(RIGHT * 3 + UP * 1.5)

        self.play(Create(cat), Create(milk), Create(cup))

        cat_drinks = Animation(cat.shift, RIGHT * 2.5 + UP * 1.5, duration=1)
        self.play(cat, cat_drinks)

        milk_pours = Animation(milk.height.set, 0, run_time=1)
        self.play(milk, milk_pours)

        self.wait(1)

        self.play(Create(Text("Milk all gone!", font_size=24, color=WHITE, fill_opacity=1).next_to(cup, DOWN * 0.5)))