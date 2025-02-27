from manim import *

class MorphHyperbola(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 25, 5],
            y_range=[0, 100, 20],
            x_length=6,
            y_length=6,
            axis_config={"color": BLUE}
        )


        k = ValueTracker(1)
        graph = always_redraw(lambda: axes.plot(
            lambda x: k.get_value() / x,
            x_range=[
                max(0.01, k.get_value()/100),
                25, 
                0.01
            ],
            color=YELLOW
        ))

        label = always_redraw(lambda: Tex(f"$f(x) = \\frac{{{int(k.get_value())}}}{{x}}$").move_to(axes.c2p(10, 40)))
        self.play(Create(axes), Create(graph), Write(label))
        self.wait(3)
        self.play(k.animate.set_value(49), run_time=10)
        self.wait(2)
