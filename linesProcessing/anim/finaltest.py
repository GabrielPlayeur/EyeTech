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



        #label33_1= Tex("33 %").next_to(line33_1).scale(sz[0])
        #label33_2= Tex("33 %").next_to(line33_2).scale(sz[0])
        #label66_1= Tex ("66 %").next_to(line66_1).scale(sz[0])
        #label66_2= Tex ("66 %").next_to(line66_2).scale(sz[0])
        #label100_1= Tex ("100 %").next_to(line100_1).scale(sz[0])
        #label100_2= Tex ("100 %").next_to(line100_2).scale(sz[0])

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
        
        self.play(Create(line0))
        self.wait()
        self.play(Uncreate(line0),lineRED.animate.put_start_and_end_on(p100_UL,p100_DL),
                  linered.animate.put_start_and_end_on(p100_UR,p100_DR))
        self.wait(2)
        self.play(lineYELLOW.animate.put_start_and_end_on(p66_UR,p66_DR),lineGREEN.animate.put_start_and_end_on(p33_UR,p33_DR),
                  lineyellow.animate.put_start_and_end_on(p66_UL,p66_DL),linegreen.animate.put_start_and_end_on(p33_UL,p33_DL))
        self.wait()
        self.play(DrawBorderThenFill(zoneGREEN))
        self.play(DrawBorderThenFill(zoneYELLOW_L),DrawBorderThenFill(zoneYELLOW_R))
        self.play(DrawBorderThenFill(zoneRED_L),DrawBorderThenFill(zoneRED_R))
        self.wait()

        
    
