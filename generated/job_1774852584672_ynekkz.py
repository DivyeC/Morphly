from manim import *

class Main(Scene):
    def construct(self):
        class OperatorNode(Rect):
            def __init__(self, operator, **kwargs):
                self.operator = operator
                super().__init__(**kwargs)
                self.add(TextMobject(self.operator).next_to(self.get_center(), UP))

        class FlowchartNode(VGroup):
            def __init__(self, node_type, input_mobject=None, output_mobject=None, **kwargs):
                super().__init__(**kwargs)
                self.node_type = node_type
                self.input = input_mobject if input_mobject else Dot()
                self.output = output_mobject if output_mobject else Dot()
                self.input.next_to(self.get_left(), DOWN)
                self.output.next_to(self.get_right(), DOWN)
                self.add(self.input, self.output)

        class Arrow(VMobject):
            def __init__(self, start, end, **kwargs):
                super().__init__(**kwargs)
                self.set_start(start)
                self.set_end(end)

        input_1 = ValueTracker(0)
        input_2 = ValueTracker(0)

        plus = OperatorNode("+")
        minus = OperatorNode("-")
        times = OperatorNode("*")
        divide = OperatorNode("/")

        input_1_node = FlowchartNode("Input 1", input_1)
        input_2_node = FlowchartNode("Input 2", input_2)

        plus_node = FlowchartNode("+")
        minus_node = FlowchartNode("-")
        times_node = FlowchartNode("*")
        divide_node = FlowchartNode("/")

        plus_input = Arrow(input_1_node.output, plus.get_center())
        minus_input = Arrow(input_2_node.output, minus.get_center())
        times_input_1 = Arrow(plus.get_right(), times_node.input)
        times_input_2 = Arrow(input_2_node.output, times_node.input)
        divide_input_1 = Arrow(times_node.output, divide_node.input)
        divide_input_2 = Arrow(plus_node.output, divide_node.input