from manim import *

class Getters(Scene):
    def construct(self):
        circ = Circle().to_edge(DL)
        rec=Rectangle(color=PINK, height=2, width=1.5).to_edge(LEFT)
        arrow = always_redraw(lambda: Line(start=rec.get_bottom(), end=circ.get_top(), buff=0.1).add_tip())
        
        self.play(Create(VGroup(circ,rec)))
        self.wait()
        self.play(Create(arrow))
        self.wait()
        self.play(rec.animate.to_edge(UR), run_time=3)


class ValueTrack(Scene):
    def construct(self):

        track= ValueTracker(0)
        nombre=always_redraw(lambda: DecimalNumber().set_value(track.get_value()))

        self.play(FadeIn(nombre))
        self.wait()
        self.play(track.animate.set_value(2), run_time=6, rate_func=smooth)


class Graphe(Scene):
    def construct(self):

        plane=(
            NumberPlane(x_range=[-5, 5, 1], x_length=12, y_range=[-2, 8, 2], y_length=6)
            .to_edge(UL)
            .add_coordinates()
        )
        labels = plane.get_axis_labels(x_label="x", y_label="f(x)")
        
        parab = plane.plot(lambda x:(x**3) , x_range= [-5, 5], color = PURPLE)
        func_label = MathTex ("f(x)={x}^{3}").next_to(plane).to_edge(DR)

        self.play(DrawBorderThenFill(plane), run_time=3)
        self.play(Create(VGroup(labels,func_label)))
        self.wait()
        self.play(Create(parab), run_time= 2)
        self.wait()




class Image(Scene):
       def construct(self) : 
        imag= ImageMobject("test_image")


        self.play(SpinInFromNothing(imag))
    

