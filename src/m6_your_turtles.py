"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Braden Smith.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.delay(25)
kitty = rg.SimpleTurtle('turtle')
kitty.pen = rg.Pen('orange',7)
kitty.speed = 25
size = 50
for k in range (10):
    kitty.draw_circle(size)
    kitty.pen_up()
    kitty.right(90)
    kitty.forward(25)
    kitty.left(90)
    kitty.forward(25)
    kitty.pen_down()
    size=(size-18)/(k+1)**(1/5)
cat = rg.SimpleTurtle('turtle')
cat.pen = rg.Pen('black',9)
cat.speed = 50
size = 64.
for k in range (16):
    cat.draw_regular_polygon(3,size)
    cat.left(90)
    cat.forward(15+40*k)


