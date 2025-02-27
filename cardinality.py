from manim import *
import numpy as np

class Cardinality(Scene):
    def construct(self):
        left_set_center_x = [-1.5, -0.5, 2, 1.5]
        left_set_center_y = [1.5, -1.5, 1, 0]

        right_set_center_x = [1, 1, -1, 0]
        right_set_center_y = [-1.5, 1, -0.5, 0]
        
        # Create elements for Set A (red circles) and Set B (blue squares)
        elements_a = VGroup()
        for i in range(4):
            circle = Circle(radius=0.2, fill_opacity=1, color=RED)
            circle.move_to(LEFT*3 + left_set_center_x[i]*RIGHT + left_set_center_y[i]*UP)
            elements_a.add(circle)

        elements_b = VGroup()
        for i in range(4):
            square = Square(side_length=0.4, fill_opacity=1, color=BLUE)
            square.move_to(RIGHT*3 + right_set_center_x[i]*RIGHT + right_set_center_y[i]*UP)
            elements_b.add(square)
        
        left_set = Circle(radius=2.5, color=RED)          
        left_set.set_fill(RED, opacity=0.3) 
        left_set.shift(LEFT*3) 
        right_set = Circle(radius=2.5, color=BLUE)
        right_set.set_fill(BLUE, opacity=0.3) 
        right_set.shift(RIGHT*3)

        # Set labels
        label_a = Text("Set A").next_to(left_set, UP)
        label_b = Text("Set B").next_to(right_set, UP)

        # Show shapes and elements
        self.play(
            LaggedStart(
                Create(left_set),
                Create(right_set),
                Write(label_a),
                Write(label_b),
                lag_ratio=0.5
            )
        )
        self.play(
            LaggedStart(
                *[FadeIn(elem) for elem in elements_a],
                *[FadeIn(elem) for elem in elements_b],
                lag_ratio=0.3
            )
        )
        self.wait(1)

        # Animate elements forming columns
        elements_a.generate_target()
        elements_a.target.arrange(DOWN, buff=0.5).shift(LEFT*3)
        elements_b.generate_target()
        elements_b.target.arrange(DOWN, buff=0.5).shift(RIGHT*3)
        left_oval = Ellipse(width=2, height=5, color=RED).shift(LEFT*3)
        right_oval = Ellipse(width=2, height=5, color=BLUE).shift(RIGHT*3)

        self.play(
            MoveToTarget(elements_a),
            MoveToTarget(elements_b),
            Transform(left_set, left_oval),
            Transform(right_set, right_oval),
            run_time=3
        )
        self.wait(1)

        # Create bijection arrows
        arrows = VGroup()
        for a, b in zip(elements_a, elements_b):
            arrow = Arrow(
                a.get_right(),
                b.get_left(),
                buff=0.1,
                color=YELLOW
            )
            arrows.add(arrow)

        self.play(LaggedStart(
            *[Create(arrow) for arrow in arrows],
            lag_ratio=0.3,
            run_time=3
        ))
        
        # Add bijection text
        bijection_text = Text("One-to-One Correspondence", color=YELLOW).to_edge(DOWN)
        self.play(Write(bijection_text))
        self.wait(2)
