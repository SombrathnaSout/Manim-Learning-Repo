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