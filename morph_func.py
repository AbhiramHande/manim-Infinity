from manim import *

class MorphHyperbola(Scene):
    def construct(self):
        # Set up the axes
        axes = Axes(
            x_range=[0, 25, 5],
            y_range=[0, 100, 20],
            x_length=6,
            y_length=6,
            axis_config={"color": BLUE}
        )

        # Create a ValueTracker to animate the coefficient
        k = ValueTracker(1)

        # Create the graph that updates with the ValueTracker
        graph = always_redraw(lambda: axes.plot(
            lambda x: k.get_value() / x,
            x_range=[
                max(0.01, k.get_value()/100),  # Dynamic start based on k
                25, 
                0.01
            ],
            color=YELLOW
        ))

        # Create a dynamic label that follows the graph
        label = always_redraw(lambda: Tex(f"$f(x) = \\frac{{{int(k.get_value())}}}{{x}}$").move_to(axes.c2p(10, 40)))

        # Animation sequence
        self.play(Create(axes), Create(graph), Write(label))
        self.wait(3)
        self.play(k.animate.set_value(49), run_time=10)
        self.wait(2)from manim import *

class MorphHyperbola(Scene):
    def construct(self):
        # Set up the axes
        axes = Axes(
            x_range=[0, 25, 5],
            y_range=[0, 100, 20],
            x_length=6,
            y_length=6,
            axis_config={"color": BLUE}
        )

        # Create a ValueTracker to animate the coefficient
        k = ValueTracker(1)

        # Create the graph that updates with the ValueTracker
        graph = always_redraw(lambda: axes.plot(
            lambda x: k.get_value() / x,
            x_range=[
                max(0.01, k.get_value()/100),  # Dynamic start based on k
                25, 
                0.01
            ],
            color=YELLOW
        ))

        # Create a dynamic label that follows the graph
        label = always_redraw(lambda: Tex(f"$\\frac{{{int(k.get_value())}}}{{x}}$").next_to(
            axes.c2p(2, k.get_value()/2), UP
        ))

        # Animation sequence
        self.play(Create(axes), Create(graph), Write(label))
        self.wait(3)
        self.play(k.animate.set_value(49), run_time=10)
        self.wait(2)
