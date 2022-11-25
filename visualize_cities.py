# Author:Chipo
# Date:11/5/2022
# Purpose:Visualize cities

from cs1lib import *
from Visualize_cities.sort_cities import rlist

W = 10
H = 10
Longitude=360
Latitude=180
max_show = 50
shown = 0


def my_draw():
    global shown

    set_clear_color(1, 1, 1)

    # To display picture
    img = load_image("../ShortAssignments/world.png")
    draw_image(img, 0, 0)

    if shown < max_show:
        for i in range(0, shown):
            draw_rect(i)
        shown = shown + 1

    else:  # To draw all of them very fast and at once
        for i in range(0, shown):
            draw_rect(i)


# Drawing rectangles
def draw_rect(n):
    set_fill_color(1, 1, 0)

    # putting the exact location in the center of the rectangle
    c = rlist[n]
    draw_rectangle(Longitude + 2 * int(c.longitude) - H // 2, Latitude - 2 * int(c.latitude) - W // 2, W, H)


start_graphics(my_draw, width=720, height=360)
