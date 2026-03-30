from manim import *

class Main(Scene):
    def construct(self):
        class OperatorNode(Rect):
            def __init__(self, operator, **kwargs):
                self.operator = operator
                super().__init__(**kwargs)
                self.add(TextMobject(self.operator).next_to(self.get_center(), UP))

        class FlowchartNode(VGroup):
            def __init__(self, node_type, input_mobjects=None, output_mobject=None, **kwargs):
                super().__init__(**kwargs)
                self.node_type = node_type
                self.input_mobjects = input_mobjects or []
                self.output_mobject = output_mobject

                self.input_lines = [
                    Line(self.get_edge(LEFT), self.get_edge(LEFT), color=GREEN)
                    for _ in range(len(self.input_mobjects))
                ]
                for line in self.input_lines:
                    line.add_updater(lambda m: m.become(Line(self.get_edge(LEFT), self.get_edge(LEFT), color=GREEN)))

                self.output_line = None
                if self.output_mobject is not None:
                    self.output_line = Line(self.get_edge(RIGHT), self.output_mobject.get_center(), color=GREEN)

                self.create_node()

            def create_node(self):
                if self.node_type == "Start":
                    self.mobject = TextMobject("Start")
                elif self.node_type == "End":
                    self.mobject = TextMobject("End")
                elif self.node_type == "Input":
                    self.mobject = TextMobject("Input")
                    self.mobject.next_to(self.get_edge(LEFT), DOWN)
                elif self.node_type == "Output":
                    self.mobject = TextMobject("Output")
                    self.mobject.next_to(self.get_edge(RIGHT), DOWN)
                elif self.node_type == "Operator":
                    self.mobject = OperatorNode(self.node_type.capitalize())
                else:
                    self.mobject = TextMobject(self.node_type)

                self.add(self.mobject)