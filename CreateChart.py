from bokeh.plotting import figure, show
from Frame import Frame
from bokeh.palettes import inferno
import itertools
class CreateChart:
    def __init__(self):
        self.frames = []
        self.numlines = 0
    def add_frame(self, frame):
        self.frames.append(frame)
        self.numlines = self.numlines + 1
        self.colors = itertools.cycle(inferno(self.numlines))

    def draw(self):
        p = figure(title="Simple line example", x_axis_label='x', y_axis_label='y')
        for frame in self.frames:
            print('drawing frame ' + frame.name)
            self.draw_frame(p, frame)
        show(p)

    def draw_frame(self, p, frame):
        l_seattube_setback, l_seattube_height, l_reach, l_stack = frame.get_points()
        x = [0, l_reach, -l_seattube_setback,  0]
        y = [0, l_stack, l_seattube_height, 0]
        p.line(x, y, legend_label=frame.name, line_width=2,
               line_color=next(self.colors))
