from manim import *

class squaretocircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(BLUE, opacity=0.5)  # set the color and transparency
        square = Square() # create a square
        square.rotate(PI/4) # rotate the square by 45 degrees
        
        self.play(Create(square)) # animate the creation of the square
        self.play(Transform(square, circle)) # animate the transformation of the square into a circle
        self.play(FadeOut(square)) # animate the fading out of the square

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, UP, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen


class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))
        self.play(Transform(square, circle))
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5) # change the color of the circle with animation
        )

class DifferentRotation(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2*LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2*RIGHT)

        self.play(left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_times=2) # left square rotates 180 degrees, right square rotates 180 degrees but left square rotates inward
        self.wait()

class TwoTransform(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(Transform(a,b))
        self.play(Transform(b,c))
        self.play(FadeOut(a))
    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a,b))
        self.play(ReplacementTransform(b,c))
        self.play(FadeOut(a))
    def construct(self):
        self.transform()
        self.wait(0.5)
        self.replacement_transform()

class TransformCycle(Scene):
    def construct(self):
        a = Circle()
        t1 = Square()
        t2 = Triangle()
        self.add(a)
        self.wait()
        for t in [t1,t2]:
            self.play(Transform(a,t))