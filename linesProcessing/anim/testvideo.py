from manim import *

class Getters(Scene):
    def construct(self):
        circle = Circle().to_edge(DL)
        
        rec=Rectangle(color=PINK, height=2, width=1).to_edge(LEFT)
        
        arr=always_redraw(lambda : Line(start=rec.get_edge_center, end=circle.get_left, buff=0.1))
        
        self.play(Create(VGroup(rec,arr,circle)))
        self.wait()
        self.play(rec.animate.to_edge(RIGHT))

