from manim import *

class Main(Scene):
    def construct(self):
        arrows = VGroup(*[Arrow(start=ORIGIN, end=self.camera.position.to_vector()*i, color=YELLOW) for i in range(1, 11)])
        arrows.set_height(1)

        operators = VGroup()

        # Unary operators
        unary_op_1 = Tex("+").next_to(arrows[0], DOWN)
        operators.add(unary_op_1)
        unary_op_2 = Tex("-").next_to(arrows[1], DOWN)
        operators.add(unary_op_2)
        unary_op_3 = Tex("!").next_to(arrows[2], DOWN)
        operators.add(unary_op_3)

        # Binary operators
        binary_op_1 = Tex("+").next_to(arrows[3], DOWN)
        operators.add(binary_op_1)
        binary_op_2 = Tex("-").next_to(arrows[4], DOWN)
        operators.add(binary_op_2)
        binary_op_3 = Tex("*").next_to(arrows[5], DOWN)
        operators.add(binary_op_3)
        binary_op_4 = Tex("/").next_to(arrows[6], DOWN)
        operators.add(binary_op_4)
        binary_op_5 = Tex("%").next_to(arrows[7], DOWN)
        operators.add(binary_op_5)
        binary_op_6 = Tex("==").next_to(arrows[8], DOWN)
        operators.add(binary_op_6)
        binary_op_7 = Tex("!=").next_to(arrows[9], DOWN)
        operators.add(binary_op_7)

        self.play(Create(arrows), Create(operators))
        self.wait(1)