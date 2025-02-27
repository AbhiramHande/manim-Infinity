from manim import *

class InfiniteSet(Scene):
    def construct(self):
        main_set = Ellipse(width=2, height=6, color=BLUE).shift(LEFT*3)
        main_set.set_fill(BLUE, opacity=0.3)
        main_label = Text("Set A").next_to(main_set, UP)

        subset = Ellipse(width=1, height=3, color=GREEN)
        subset.move_to(main_set.get_center())

        subset_new = Ellipse(width=2, height=6, color=GREEN).shift(RIGHT*3)
        subset_new.set_fill(GREEN, opacity=0.3)
        subset_label = MathTex("B \subset A").next_to(subset_new, UP)
        
        self.play(Create(main_set), Write(main_label))
        self.wait(2)  
        self.play(Create(subset))
        self.wait(1)
        self.play(
            Transform(subset, subset_new),
            Write(subset_label)
        )
        self.wait(2)
        
        arrow = DoubleArrow(
            main_set.get_right(),
            subset.get_left(),
            color=YELLOW,
            stroke_width=4,
            tip_length=0.2
        )
        self.play(Create(arrow))
        self.wait(2)

        self.play(
            FadeOut(arrow),
            FadeOut(main_set),
            FadeOut(subset),
            FadeOut(main_label),
            FadeOut(subset_label)
        )
        self.wait(1)
