from CalcGeo import calc_slope
class Frame:
    def __init__(self, name_in, l_seattube_in, ang_seattube_in, 
                 l_reach_in, l_stack_in):
        self.name = name_in
        self.l_seattube = l_seattube_in
        self.ang_seattube = ang_seattube_in
        self.l_reach = l_reach_in
        self.l_stack = l_stack_in

    def get_points(self):
        return calc_slope(
                self.l_seattube, 
                self.ang_seattube, 
                self.l_reach,
                self.l_stack)     

