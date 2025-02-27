from manim import *

class BijectionNaturalEven(Scene):
    def construct(self):
        title = Text("Bijection: Natural Numbers ↔ Even Numbers", font_size=32)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        self.wait(0.5)

        left_oval = Ellipse(width=2, height=5, color=BLUE).shift(LEFT*3)
        right_oval = Ellipse(width=2, height=5, color=RED).shift(RIGHT*3)
        natural_label = MathTex("\mathbb{N}", color=BLUE).next_to(left_oval, DOWN)
        even_label = MathTex("2\mathbb{N}", color=RED).next_to(right_oval, DOWN)

        naturals = VGroup(*[Text(str(n)) for n in range(1, 5)] + [Text("⋮")])
        evens = VGroup(*[Text(str(2*n)) for n in range(1, 5)] + [Text("⋮")])
        naturals.arrange(DOWN, buff=0.5).move_to(left_oval)
        evens.arrange(DOWN, buff=0.5).move_to(right_oval)

        self.play(
            Create(left_oval),
            Create(right_oval),
            Write(natural_label),
            Write(even_label),
            run_time=1.5
        )
        self.wait(0.5)
        
        self.play(
            LaggedStart(*[FadeIn(n) for n in naturals], lag_ratio=0.3),
            LaggedStart(*[FadeIn(e) for e in evens], lag_ratio=0.3),
            run_time=2
        )
        self.wait(1)

        arrows = VGroup()
        for n, e in zip(naturals[:-1], evens[:-1]):
            arrow = Arrow(
                n.get_right(),
                e.get_left(),
                buff=0.1,
                color=YELLOW,
                max_tip_length_to_length_ratio=0.15
            )
            arrows.add(arrow)

        self.play(
            LaggedStart(*[Create(arrow) for arrow in arrows], lag_ratio=0.3),
            run_time=3
        )
        self.wait(1)

        general_rule = MathTex("f(x) = 2x", color=GREEN).scale(1.5)
        general_rule.move_to(DOWN*2)
        
        general_arrow = Arrow(
            left_oval.get_right(),
            right_oval.get_left(),
            color=YELLOW
        ).shift(UP*0.5)
        label = MathTex("x \mapsto 2x").next_to(general_arrow, UP, buff=0.1)


        self.play(FadeOut(arrows), run_time=2)
        self.play(
            FadeIn(general_arrow),
            Write(label),
            run_time=2
        )
        self.wait(5)
