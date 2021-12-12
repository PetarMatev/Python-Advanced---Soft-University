from canvas import tk


def clean_screen():
    for el in tk.grid_salves():
        el.destroy()