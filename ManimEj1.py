from manim import *

class FirstScene(Scene):

    def construct(self):
        sq = Square()
        circ = Circle().set_fill(opacity=1)
        self.play(Transform(sq, circ))
        self.wait() 
#Revisado
#Profa.Hazem AR
