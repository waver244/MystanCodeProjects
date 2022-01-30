"""
File: babygraphics.py
Name: Yin Jun (Ingrid) Zeng
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    distance = (width-GRAPH_MARGIN_SIZE*2)/len(YEARS)
    x = GRAPH_MARGIN_SIZE + distance * year_index
    return x


def get_y_coordinate(height, rank):
    """
    Given the height of the canvas and the rank of the current year
    returns the y coordinate where the rank should be drawn.

    Input:
        height (int): The height of the canvas
        rank (str): The rank number
    Returns:
        y_coordinate (int): The y coordinate of the rank.
    """
    pass


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=str(YEARS[i]), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    for j in range(len(lookup_names)):
        # Find the name to check
        name_to_check = lookup_names[j]
        # Define colors
        color = ''
        if j % 4 == 0:
            color = COLORS[0]
        elif j % 4 == 1:
            color = COLORS[1]
        elif j % 4 == 2:
            color = COLORS[2]
        elif j % 4 == 3:
            color = COLORS[3]
        if name_to_check in name_data:
            for i in range(len(YEARS)):
                # Rank in top1000
                if str(YEARS[i]) in name_data[name_to_check]:
                    rank = name_data[name_to_check][str(YEARS[i])]
                    x = get_x_coordinate(CANVAS_WIDTH, i)
                    y = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE * 2) / MAX_RANK * int(rank)
                    show = name_to_check + str(" ") + rank  # Info to be displayed
                # Out of rank list
                else:
                    x = get_x_coordinate(CANVAS_WIDTH, i)
                    y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    show = name_to_check + '*'  # Info to be displayed
                if i != len(YEARS)-1:
                    # Rank in top1000
                    if str(YEARS[i+1]) in name_data[name_to_check]:
                        next_rank = name_data[name_to_check][str(YEARS[i+1])]
                        next_x = get_x_coordinate(CANVAS_WIDTH, i+1)
                        next_y = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE * 2) / MAX_RANK * int(next_rank)
                    # Out of rank list
                    else:
                        next_x = get_x_coordinate(CANVAS_WIDTH, i + 1)
                        next_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    canvas.create_line(x, y, next_x, next_y, width=LINE_WIDTH, fill=color)
                    canvas.create_text(x+TEXT_DX, y, text=show, anchor=tkinter.SW, fill=color)
                # Last year
                else:
                    canvas.create_text(x+TEXT_DX, y, text=show, anchor=tkinter.SW, fill=color)


def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
