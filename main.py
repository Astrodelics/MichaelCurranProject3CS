import arcade
#This opens the arcade interpretor in Python.
arcade.open_window(900, 900, "Symmetry")
#This opens the window where the picture we are creating will appear.
arcade.start_render()
#This starts rendering the code we typed into the window.
arcade.draw_lrtb_rectangle_filled(50, 400, 450, 0, arcade.color.BLUE_YONDER)
arcade.draw_lrtb_rectangle_filled(500, 850, 900, 450, arcade.color.BLUE_YONDER)
#These two lines draw the blue rectangles in the arcade window.
arcade.draw_circle_outline(200, 700, 100, arcade.color.BLUE_YONDER)
arcade.draw_circle_outline(650, 200, 100, arcade.color.BLUE_YONDER)
#These two lines draw the blue circles in the arcade window.
arcade.draw_line(5, 450, 895, 450, arcade.color.RED_DEVIL, 4)
#This line draws the red line in the arcade window.
arcade.draw_parabola_filled(400, 375, 500, 100, arcade.color.YELLOW_ROSE)
arcade.draw_parabola_filled(400, 525, 500, -100, arcade.color.YELLOW_ROSE)
#These two lines draw the yellow parabolas in the arcade window.
arcade.draw_arc_outline(600, 700, 100, 100, arcade.color.GUPPIE_GREEN, -180, 0, 10)
arcade.draw_arc_outline(300, 200, 100, 100, arcade.color.GUPPIE_GREEN, -180, 0, 10)
#These two lines draw the green arcs in the arcade window.
arcade.draw_lrtb_rectangle_outline(200, 400, 400, 0, arcade.color.BLACK_OLIVE)
arcade.draw_lrtb_rectangle_outline(500, 700, 900, 500, arcade.color.BLACK_OLIVE)
#These two lines draw the black rectangle outlines in the arcade window.
arcade.draw_text("Michael Curran", 360, 445, arcade.color.PURPLE_PIZZAZZ, 20, 100)
#This line of code draws the text in the middle of the arcade window.
arcade.finish_render()
#This stops rendering the code we typed into the window.
arcade.run()
#This runs the arcade code we typed in.