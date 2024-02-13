from manim import *

#__________________________________________________SEGMENTATION DE LA PISTE_______________________________________________________#

class Lines(Scene):
    def construct (self):
    
        c=[RED, # border color
           GREEN, # middle
           YELLOW, # intermediate
           ORANGE,
           WHITE
           ]
        sz=[[0.5], #text
            [5], #1st line size
            [10] #2nd line
            ]
        font=["sans-serif"
              ]

        p0_U=np.array([2, 4, 0])
        p0_D=np.array([-2, -4, 0])
        p33_UR=np.array([3, 4, 0])
        p33_DR=np.array([-1, -4, 0])
        p33_UL=np.array([1, 4, 0])
        p33_DL=np.array([-3, -4, 0])

        p66_UR=np.array([4.5, 4, 0])
        p66_DR=np.array([0.5, -4, 0])
        p66_UL=np.array([-0.5, 4, 0])
        p66_DL=np.array([-4.5, -4, 0])

        p100_UR=np.array([6, 4, 0])
        p100_DR=np.array([2, -4, 0])
        p100_UL=np.array([-2, 4, 0])
        p100_DL=np.array([-6, -4, 0])
        
        line0=Line(start=p0_U, end=p0_D).scale(sz[1])
        
        lineRED=Line(color=c[0], start=p0_U, end=p0_D).scale(sz[2])
        linered=Line(color=c[0], start=p0_U, end=p0_D).scale(sz[2])
        lineYELLOW=DashedLine(color=c[2], start=p0_U, end=p0_D, dashed_ratio=0.1).scale(sz[2])
        lineyellow=DashedLine(color=c[2], start=p0_U, end=p0_D, dashed_ratio=0.1).scale(sz[2])
        lineGREEN=DashedLine(color=c[1], start=p0_U, end=p0_D, dashed_ratio=0.1).scale(sz[2])
        linegreen=DashedLine(color=c[1], start=p0_U, end=p0_D, dashed_ratio=0.1).scale(sz[2])



        labelzoneGREEN= Text("0 %",color=c[4], font="sans-serif").next_to((p33_UL+p33_DL)/3, UR).scale(sz[0])
        labelzoneYELLOW_L= Text("33 %",color=c[4], font="sans-serif").next_to((p66_UL+p66_DL)/2, UR).scale(sz[0])
        labelzoneRED_L= Text("66 %",color=c[4], font="sans-serif").next_to((p100_UL+p100_DL)/2, UR).scale(sz[0])
        labelzonemax_L= Text("100 %",color=c[4], font="sans-serif").next_to((p100_UL+p100_DL)/2, UL).scale(sz[0])

        labelzoneYELLOW_R= Text("33 %",color=c[4], font="sans-serif").next_to((p33_UR+p33_DR)/2, UR).scale(sz[0])
        labelzoneRED_R= Text("66 %",color=c[4], font="sans-serif").next_to((p66_UR+p66_DR)/2, UR).scale(sz[0])
        labelzonemax_R= Text("100 %",color=c[4], font="sans-serif").next_to((p100_UR+p100_DR)/2, UR).scale(sz[0])


        position_GREEN = [
            p33_UR,  # top right
            p33_DR,  # bottom right
            p33_DL,  # bottom left
            p33_UL,  # top left
        ]
        zoneGREEN = Polygon(*position_GREEN, color=c[1], fill_color=c[1],fill_opacity=0.5)

        position_YELLOW_L = [
            p33_UL,  # top right
            p33_DL,  # bottom right
            p66_DL,  # bottom left
            p66_UL,  # top left
        ]
        zoneYELLOW_L = Polygon(*position_YELLOW_L, color=c[2], fill_color=c[2],fill_opacity=0.5)
        
        position_YELLOW_R = [
            p33_UR,  # top right
            p33_DR,  # bottom right
            p66_DR,  # bottom left
            p66_UR,  # top left
        ]
        zoneYELLOW_R = Polygon(*position_YELLOW_R, color=c[2], fill_color=c[2],fill_opacity=0.5)

        position_RED_L = [
            p66_UL,  # top right
            p66_DL,  # bottom right
            p100_DL,  # bottom left
            p100_UL,  # top left
        ]
        zoneRED_L = Polygon(*position_RED_L, color=c[0], fill_color=c[3],fill_opacity=0.5)

        position_RED_R = [
            p66_UR,  # top right
            p66_DR,  # bottom right
            p100_DR,  # bottom left
            p100_UR,  # top left
        ]
        zoneRED_R = Polygon(*position_RED_R, color=c[0], fill_color=c[3],fill_opacity=0.5)

        
        ##############################################SCENARIO#####################################################
        self.wait()
        self.play(Create(line0))
        self.wait()
        self.play(Uncreate(line0),lineRED.animate.put_start_and_end_on(p100_UL,p100_DL),
                  linered.animate.put_start_and_end_on(p100_UR,p100_DR))
        self.wait(2)
        self.play(lineYELLOW.animate.put_start_and_end_on(p66_UR,p66_DR),lineGREEN.animate.put_start_and_end_on(p33_UR,p33_DR),
                  lineyellow.animate.put_start_and_end_on(p66_UL,p66_DL),linegreen.animate.put_start_and_end_on(p33_UL,p33_DL))
        self.wait()
        self.play(DrawBorderThenFill(zoneGREEN))
        self.play(DrawBorderThenFill(zoneYELLOW_L),DrawBorderThenFill(zoneYELLOW_R),Write(labelzoneGREEN))
        self.play(DrawBorderThenFill(zoneRED_L),DrawBorderThenFill(zoneRED_R),Write(VGroup(labelzoneYELLOW_L,labelzoneYELLOW_R)))
        self.play(Write(VGroup(labelzoneRED_L,labelzoneRED_R)))
        self.play(Write(VGroup(labelzonemax_L,labelzonemax_R)))
        self.wait()

        
    
#_______________________________________________________CAMERA / HOUGH___________________________________________________________#
        
class Hough(Scene):
    def construct (self):

        c=[BLUE,
           GREEN
           ]

        Eq = VGroup(
            MathTex("y_i", "=", "a", "x_i", "+","b"),
            MathTex("b", "=", "-a", "x_i", "+","y_i")
        )
        Eq.arrange(buff=LARGE_BUFF)
        for line in Eq:
            line.set_color_by_tex_to_color_map({
                "y_i": BLUE,
                "x_i": BLUE,
                "a": GREEN,
                "b": GREEN,
            })

        arrow = always_redraw(lambda: Line(start=Eq[0].get_right(), end=Eq[1].get_left(), buff=1).add_tip())
        

        plane_Eq_Image=(
            Axes(
                x_range=[-1, 8], y_range=[-1, 8], x_length=5, y_length=5,
                axis_config={"font_size": 24}
                )
            .to_edge(LEFT)
            .add_coordinates()
        )

        labels_Eq_Image = plane_Eq_Image.get_axis_labels(x_label="x", y_label="y")
        func_label_Eq_Image = Text ("Image Space",color=c[0], font="sans-serif").next_to(plane_Eq_Image).to_edge(UL).scale(0.5)

        plane_Eq_Parameter=(
            Axes(
                x_range=[-1, 8], y_range=[-1, 8], x_length=5, y_length=5,
                axis_config={"font_size": 24}
                )
            .to_edge(RIGHT)
            #.add_coordinates()
        )

        labels_Eq_Parameter = plane_Eq_Parameter.get_axis_labels(x_label="a", y_label="b")
        func_label_Eq_Parameter = Text ("Parameter Space",color=c[1], font="sans-serif").next_to(plane_Eq_Parameter).to_edge(UR).scale(0.5)

        a=1/3
        b=1
        MainLine = plane_Eq_Image.plot(lambda x : (a)*x+b,  
                                    color = c[0],
                                    )
        dashed_line=DashedVMobject(MainLine)

        Crosspoint=Dot(plane_Eq_Parameter.coords_to_point(a, b), color=c[1])
        Tex_Crosspoint=MathTex(r"\left(\frac{1}{3},1\right)").scale(0.75).next_to(plane_Eq_Parameter.c2p(a, b))
        lines_Crosspoint = plane_Eq_Parameter.get_lines_to_point(plane_Eq_Parameter.c2p(a,b))
        Cross=VGroup(Crosspoint,Tex_Crosspoint,lines_Crosspoint)

        fake_x=1
        fake_y=5
        Fakepoint=Dot(plane_Eq_Image.c2p(fake_x,fake_y))
        curve_Fakepoint=plane_Eq_Parameter.plot(lambda x: -fake_x*x+fake_y)
        
            

##############################################SCENARIO#####################################################
        self.wait()
        self.play(Write(Eq[0].to_edge(LEFT)))
        self.wait()
        self.add(arrow)
        self.play(TransformMatchingTex(Eq[0].copy(),Eq[1].to_edge(RIGHT),
                                       path_arc=90 * DEGREES, run_time=2))
        self.wait()
        self.play(Eq[0].animate.to_edge(DL),Eq[1].animate.to_edge(DR))
        self.wait()
        self.play(DrawBorderThenFill(plane_Eq_Image), DrawBorderThenFill(plane_Eq_Parameter), run_time=3)
        self.wait()
        self.play(Create(VGroup(labels_Eq_Image,labels_Eq_Parameter,func_label_Eq_Image,func_label_Eq_Parameter)))
        self.wait()
        pt_x=0
        pt_y=1
        for i in np.arange(1, 5,1):
            pt_x=pt_x+1.5
            pt_y=pt_y+0.5
            dot=Dot(plane_Eq_Image.c2p(pt_x,pt_y))
            curve=(plane_Eq_Parameter.plot(lambda x: -pt_x*x+pt_y))
            self.play(Create(dot))
            self.wait()
            self.add((curve))
            self.wait()
        self.play(Create(Cross))
        self.wait()
        self.play(Create(dashed_line))
        self.wait()
        self.play(Create(Fakepoint))
        self.wait()
        self.play(Create(curve_Fakepoint))
        self.wait()

