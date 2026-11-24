from manim import *

class Main(Scene):
    def construct(self):
        title = Text("Water Cycle", font_size=40).to_edge(UP)
        self.play(Write(title))

        # Nodes
        evaporation = Text("Evaporation", font_size=24)
        condensation = Text("Condensation", font_size=24)
        precipitation = Text("Precipitation", font_size=24)
        collection = Text("Collection", font_size=24)
        transpiration = Text("Transpiration", font_size=24)

        evap_pos = LEFT * 4 + UP * 1.5
        cond_pos = LEFT * 1 + UP * 2.5
        precip_pos = RIGHT * 2.5 + UP * 2
        coll_pos = RIGHT * 2.5 + DOWN * 1
        transp_pos = LEFT * 4 + DOWN * 1.5

        evaporation.move_to(evap_pos)
        condensation.move_to(cond_pos)
        precipitation.move_to(precip_pos)
        collection.move_to(coll_pos)
        transpiration.move_to(transp_pos)

        # Boxes
        evap_box = SurroundingRectangle(evaporation, color=BLUE, buff=0.15)
        cond_box = SurroundingRectangle(condensation, color=TEAL, buff=0.15)
        precip_box = SurroundingRectangle(precipitation, color=GREEN, buff=0.15)
        coll_box = SurroundingRectangle(collection, color=YELLOW, buff=0.15)
        transp_box = SurroundingRectangle(transpiration, color=ORANGE, buff=0.15)

        # Arrows
        arrow1 = Arrow(evap_box.get_top(), cond_box.get_left(), buff=0.1, color=WHITE)
        arrow2 = Arrow(cond_box.get_right(), precip_box.get_top(), buff=0.1, color=WHITE)
        arrow3 = Arrow(precip_box.get_bottom(), coll_box.get_top(), buff=0.1, color=WHITE)
        arrow4 = Arrow(coll_box.get_left(), transp_box.get_right(), buff=0.1, color=WHITE)
        arrow5 = Arrow(transp_box.get_top(), evap_box.get_bottom(), buff=0.1, color=WHITE)

        # Animation sequence
        self.play(Create(evap_box), Write(evaporation))
        self.play(Create(arrow1), Create(cond_box), Write(condensation))
        self.play(Create(arrow2), Create(precip_box), Write(precipitation))
        self.play(Create(arrow3), Create(coll_box), Write(collection))
        self.play(Create(arrow4), Create(transp_box), Write(transpiration))
        self.play(Create(arrow5))