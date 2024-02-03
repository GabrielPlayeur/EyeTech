from manim import *

class Lines(Scene):
    def construct (self):
    
        c=[RED, # border color
           GREEN, # middle
           YELLOW, # intermediate
           ORANGE
           ]
        sz=[[0.5], #text
            [5], #1st line size
            [10] #2nd line
            ]
        ang=[[20]]

        line0=Line().rotate(ang[0]).scale(sz[1])
        line100_1=Line(color=c[0]).rotate(ang[0]).scale(sz[1])
        line100_2=Line(color=c[0]).rotate(ang[0]).scale(sz[1])
        line33_1=Line(color=c[1]).rotate(ang[0]).scale(sz[2])
        line33_2=Line(color=c[1]).rotate(ang[0]).scale(sz[2])
        line66_1=Line(color=c[2]).rotate(ang[0]).scale(sz[2])
        line66_2=Line(color=c[2]).rotate(ang[0]).scale(sz[2])

        label33_1= Tex("33 %").next_to(line33_1).scale(sz[0])
        label33_2= Tex("33 %").next_to(line33_2).scale(sz[0])
        label66_1= Tex ("66 %").next_to(line66_1).scale(sz[0])
        label66_2= Tex ("66 %").next_to(line66_2).scale(sz[0])
        label100_1= Tex ("100 %").next_to(line100_1).scale(sz[0])
        label100_2= Tex ("100 %").next_to(line100_2).scale(sz[0])

        position_list0 = [
            [2.9, 4, 0],  # top right
            [-0.7, -4, 0],  # bottom right
            [-2.9, -4, 0],  # bottom left
            [0.7, 4, 0],  # top left
        ]
        zone0 = Polygon(*position_list0, color=c[1], fill_color=c[1],fill_opacity=0.5)

        position_list33_1 = [
            [0.7, 4, 0],  # top right
            [-2.9, -4, 0],  # bottom right
            [-4.53, -4, 0],  # bottom left
            [-1, 4, 0],  # top left
        ]
        zone33_1 = Polygon(*position_list33_1, color=c[2], fill_color=c[2],fill_opacity=0.5)

        position_list66_1 = [
            [-1, 4, 0],  # top right
            [-4.53, -4, 0],  # bottom right
            [-6.35, -4, 0],  # bottom left
            [-2.82, 4, 0],  # top left
        ]
        zone66_1 = Polygon(*position_list66_1, color=c[3], fill_color=c[3],fill_opacity=0.5)

        
        ##############################################SCENARIO#####################################################
        
        self.play(Create(VGroup(line0,line100_1,line100_2)))
        self.wait()
        self.play(Uncreate(line0),line100_1.animate.next_to(line0).to_edge(LEFT),line100_2.animate.next_to(line0).to_edge(RIGHT))
        self.wait(2)
        self.play(line66_2.animate.move_to(5),line33_2.animate.move_to(2),
                  line66_1.animate.move_to(-5),line33_1.animate.move_to(-2))
        self.wait()
        self.add(zone0,zone33_1,zone66_1)

        self.wait()

        
    
