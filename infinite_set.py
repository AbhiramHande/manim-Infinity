from manim import *

class InfiniteSet(Scene):
    def construct(self):
        # Create main set S
        main_elements = VGroup(
            Tex("1"), Tex("2"), Tex("3"), 
            Tex("4"), Tex("5"), Tex("6"), 
            Tex("\\vdots")
        ).arrange(DOWN, buff=0.3).shift(LEFT * 3)
        main_ellipse = Ellipse(width=1, height=2, color=BLUE).surround(main_elements)
        
        self.play(Create(main_ellipse), Write(main_elements))
        self.wait(2)
        
        # Create subset elements (even numbers)
        subset_indices = [1, 3, 5, 6]  # Indices of 2, 4, 6, ⋮
        subset_elements = VGroup(*[
            main_elements[i].copy().set_color(GREEN) 
            for i in subset_indices
        ])
        subset_ellipse = Ellipse(width=1.5, height=3, color=GREEN).surround(subset_elements)
        
        self.play(
            FadeIn(subset_elements),
            Create(subset_ellipse),
            main_elements.animate.set_opacity(0.5)
        )
        self.wait(2)
        
        # Move subset to the right
        subset_group = VGroup(subset_ellipse, subset_elements)
        subset_group.generate_target()
        subset_group.target.shift(RIGHT * 3)
        subset_ellipse_target = subset_ellipse.copy().scale(1.2)
        subset_group.target[0] = subset_ellipse_target
        
        self.play(
            MoveToTarget(subset_group),
            main_ellipse.animate.set_opacity(0.3),
            run_time=2
        )
        self.wait(2)
        
        # Draw bijection arrows
        arrows = VGroup()
        for i in range(3):  # Connect 2→1, 4→2, 6→3
            arrow = Arrow(
                subset_elements[i].get_left(),
                main_elements[i].get_right(),
                buff=0.1,
                color=YELLOW
            )
            arrows.add(arrow)
        
        self.play(LaggedStart(*[Create(arrow) for arrow in arrows], lag_ratio=0.5))
        self.wait(2)
        
        # Display bijection function
        bijection_label = Tex("$f(n) = \\frac{n}{2}$", color=YELLOW)
        bijection_label.next_to(arrows, DOWN, buff=0.5)
        self.play(Write(bijection_label))
        self.wait(3)