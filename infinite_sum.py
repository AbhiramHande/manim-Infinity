from manim import *

class GeometricSeries(Scene):
    def construct(self):
        # Write the equation and move to top
        title = MathTex(r"\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + \frac{1}{32} + \cdots = \quad ?")
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        self.wait(0.5)

        center_group = VGroup()
        previous_right_group = None  # To track previous right-side elements
        
        # Starting dimensions (scaled down for better visibility)
        current_x, current_y = -4, -2
        center_x = [0, -1/4, 1/4, -1/8, 1/8, -1/16, 1/16, -1/32, 1/32, -1/64, 1/64, -1/128, 1/128]
        center_y = [-1/4, 1/4, -1/8, 1/8, -1/16, 1/16, -1/32, 1/32, -1/64, 1/64, -1/128, 1/128]
        scale = 3
        current_width, current_height = 3.0, 3.0

        for i in range(10):
            # Remove previous right-side elements
            if previous_right_group:
                self.play(FadeOut(previous_right_group))
                self.remove(previous_right_group)

            if i % 2 == 0:
                # Horizontal split (rectangle)
                new_height = current_height / 2
                
                # Right-side elements
                rect_right = Rectangle(width=current_width, height=new_height, color=BLUE)
                rect_right.set_fill(TEAL_A, opacity=0.2)
                rect_right.shift(RIGHT*3)
                area_label = MathTex(r"\text{Area} = \frac{1}{%d}" % (2**(i+1))).next_to(rect_right, UP)
                
                # Arrows and labels
                length_arrow = DoubleArrow(rect_right.get_left(), rect_right.get_right(), buff=0).next_to(rect_right, DOWN)
                length_label = MathTex(f"{current_width/scale:.2f}").scale(0.7).next_to(length_arrow, DOWN)
                height_arrow = DoubleArrow(rect_right.get_bottom(), rect_right.get_top(), buff=0).next_to(rect_right, LEFT)
                height_label = MathTex(f"{new_height/scale:.2f}").scale(0.7).next_to(height_arrow, LEFT)
                
                shape_group = VGroup(rect_right, area_label, length_arrow, length_label, height_arrow, height_label)
                
                # Update remaining area dimensions
                current_y += new_height
                current_height = new_height
            else:
                # Vertical split (square)
                new_width = current_width / 2
                
                # Right-side elements
                square_right = Rectangle(width=new_width, height=current_height, color=BLUE)
                square_right.set_fill(TEAL_A, opacity=0.2)
                square_right.shift(RIGHT*3)
                area_label = MathTex(r"\text{Area} = \frac{1}{%d}" % (2**(i+1))).next_to(square_right, UP)
                
                # Arrow and label
                side_arrow = DoubleArrow(square_right.get_left(), square_right.get_right(), buff=0).next_to(square_right, DOWN)
                side_label = MathTex(f"{new_width/3:.2f}").scale(0.7).next_to(side_arrow, DOWN)
                up_arrow = DoubleArrow(square_right.get_left(), square_right.get_right(), buff=0).rotate(PI/2).next_to(square_right, LEFT)
                up_label = MathTex(f"{new_width/3:.2f}").scale(0.7).next_to(side_arrow, LEFT)
                
                shape_group = VGroup(square_right, area_label, side_arrow, side_label, up_arrow, up_label)
                
                # Update remaining area dimensions
                if i != 1: current_x -= new_width
                current_width = new_width

            # Animate new right-side elements
            self.play(
                LaggedStart(
                    Create(shape_group[0]),
                    Write(shape_group[1]),
                    Create(shape_group[2]),
                    Write(shape_group[3]),
                    Create(shape_group[4]), 
                    Write(shape_group[5])
                )
            )
            self.wait(1)

            # Create center shape (invisible placeholder)

            # Copy to center
            copy_shape = shape_group[0].copy()
            center_shape = rect_right if i % 2 == 0 else square_right
            center_shape.move_to(RIGHT*(current_x - center_x[i]*scale)+ UP*(current_y + center_y[i]*scale))
            self.play(Transform(copy_shape, center_shape))
            center_group.add(copy_shape)
            self.wait()

            previous_right_group = shape_group

        
        if previous_right_group:
            self.play(FadeOut(previous_right_group))
            self.remove(previous_right_group)

        # Final bounding square
        bounding_square = Square(side_length=3, color=GREEN)
        bounding_square.move_to(4*LEFT + 0.5*DOWN)
        self.play(Create(bounding_square), run_time=2)
        self.wait()

        square = Square(side_length=scale, color=GREEN)
        square.set_fill(GREEN_A, opacity=0.3)
        square.move_to(ORIGIN)

        side_arrow = DoubleArrow(square.get_left(), square.get_right(), buff=0).next_to(square, DOWN)
        side_label = Text("1.00").scale(0.7).next_to(side_arrow, DOWN)
        up_arrow = DoubleArrow(square.get_left(), square.get_right(), buff=0).rotate(PI/2).next_to(square, LEFT)
        up_label = Text("1.00").scale(0.7).next_to(side_arrow, LEFT)

        # Fade elements and reveal result
        self.play(
            FadeOut(center_group),
            Transform(bounding_square, square),
            Create(side_arrow),
            Create(up_arrow),
            Write(side_label),
            Write(up_label),
            runtime=3
        )
        


        area_label = Text("Area = 1").move_to(3*DOWN)
        self.play(Write(area_label))
        self.wait(2)

        self.play(
            FadeOut(area_label),
            FadeOut(up_label),
            FadeOut(side_label),
            FadeOut(bounding_square),
            FadeOut(up_arrow),
            FadeOut(side_arrow),
            title.animate.move_to(ORIGIN)
        )
        self.wait(1)

        new_equation = MathTex(r"\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + \frac{1}{32} + \cdots = 1")
        self.play(Transform(title, new_equation))
        self.wait(2)