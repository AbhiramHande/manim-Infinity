#TODO. This has not been completed 
from manim import *

class ZenosParadox(Scene):
    def construct(self):
        man_start = [-4, -1, 0]
        man_end = [0, -1, 0]
        tortoise_start = [4, -1, 0]
        tortoise_end = [4.5, -1, 0]

        # Create the initial line
        line = Line(man_start, tortoise_start)
        line.set_color(ORANGE)
        line.set_opacity(0.6)
        self.play(Create(line))

        # Create glowing dots for the man and the tortoise
        man = Dot(man_start, color=BLUE, radius=0.15)
        man.set_sheen(0.8, UL)
        tortoise = Dot(tortoise_start, color=GREEN, radius=0.15)
        tortoise.set_sheen(0.8, UR)

        man_label = Text("Achilles").next_to(man, UP, buff=0.1).scale(0.8)
        man_label.add_updater(lambda m: m.next_to(man, UP, buff=0.1))
        tortoise_label = Text("Tortoise").next_to(tortoise, UP, buff=0.1).scale(0.8)
        tortoise_label.add_updater(lambda m: m.next_to(tortoise, UP, buff=0.1))

        man_target = man.copy().move_to(man_end)
        tortoise_target = tortoise.copy().move_to(tortoise_end)

        man_path = Line(man_start, man_end)
        man_path.set_color(BLUE)
        man_path.set_opacity(0.3)

        tortoise_path = Line(tortoise_start, tortoise_end)
        man_path.set_color(GREEN)
        man_path.set_opacity(0.6)
        man_path.add_to_back()

        new_line = Line(man_end, tortoise_start)
        new_line.set_color(ORANGE)
        new_line.set_opacity(0.6)

        # Move the man to the middle and slightly move the tortoise
        self.play(
            FadeIn(man, scale=1.5), 
            FadeIn(tortoise, scale=1.5),
            Write(man_label),
            Write(tortoise_label)
        )
        self.wait(1)

        self.play(
            man.animate.move_to(man_target),
            tortoise.animate.move_to(tortoise_target),
            Transform(line, new_line),
            Create(tortoise_path),
            Create(man_path),
            run_time=2
        )
        self.wait(0.5)
        
        
        # self.play(
        #     Create(man_path),
        #     Create(tortoise_path),
        #     line.animate.set_opacity(0.3)
        # )
        # self.wait(0.5)

        # Restretch the line for zoom effect
        # new_line = Line([-0.5, 0, 0], [3, 0, 0])
        # new_line.shift(DOWN)
        
        # self.play(
            
        #     man.animate.move_to([-4, -1, 0]),
        #     tortoise.animate.move_to([4, -1, 0]),
        #     FadeOut(man_path),
        #     FadeOut(tortoise_path),
        #     run_time=2
        # )
        # self.wait(1)
