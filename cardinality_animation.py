from manim import *

class CardinalityExample(Scene):
    def construct(self):
        # Title
        title = Text("Cardinality: Bijection Between Sets", font_size=32)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Create two sets
        set_a = VGroup(*[Circle(radius=0.2, fill_opacity=1, color=BLUE) for _ in range(5)])
        set_b = VGroup(*[Circle(radius=0.2, fill_opacity=1, color=RED) for _ in range(5)])
        
        # Position sets
        set_a.arrange(DOWN, center=False, aligned_edge=LEFT).shift(LEFT*3)
        set_b.arrange(DOWN, center=False, aligned_edge=RIGHT).shift(RIGHT*3)

        # Add set labels
        label_a = Text("Set A").next_to(set_a, UP)
        label_b = Text("Set B").next_to(set_b, UP)

        # Show sets
        self.play(
            LaggedStart(
                Create(set_a),
                Create(set_b),
                Write(label_a),
                Write(label_b),
                lag_ratio=0.5
            )
        )
        self.wait(0.5)

        # Create bijection arrows
        arrows = VGroup()
        for elem_a, elem_b in zip(set_a, set_b):
            arrow = Arrow(
                elem_a.get_right(),
                elem_b.get_left(),
                buff=0.1,
                color=YELLOW
            )
            arrows.add(arrow)

        # Animate arrows with numbers
        self.play(LaggedStart(
            *[Create(arrow) for arrow in arrows],
            lag_ratio=0.3,
            run_time=3
        ))
        
        # Add bijection text
        bijection_text = Text("Bijection: One-to-One Correspondence", color=YELLOW).to_edge(DOWN)
        self.play(Write(bijection_text))
        self.wait(2)
        
        # Final transformation
        conclusion = Text("Same Cardinality!", color=GREEN).scale(1.2)
        self.play(
            ReplacementTransform(bijection_text, conclusion),
            run_time=1.5
        )
        self.wait(2)