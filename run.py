from CalcGeo import calc_slope
from CreateChart import CreateChart
from Frame import Frame


cc = CreateChart()


# size 51
l_seattube = 510
ang_seattube = 75
l_reach = 375.4
l_stack = 558.5
frame = Frame("51",l_seattube, ang_seattube, l_reach, l_stack)
cc.add_frame(frame)
# size 56
l_seattube = 560
ang_seattube = 73.5
l_reach = 383.1
l_stack = 579.5
frame = Frame("56", l_seattube, ang_seattube, l_reach, l_stack)
cc.add_frame(frame)
# size 53
l_seattube = 530
ang_seattube = 74
l_reach = 381.3
l_stack = 571
frame = Frame("53", l_seattube, ang_seattube, l_reach, l_stack)
cc.add_frame(frame)
# size 48
l_seattube = 480
ang_seattube = 75
l_reach = 372
l_stack = 534
frame = Frame("48", l_seattube, ang_seattube, l_reach, l_stack)
cc.add_frame(frame)
# size 42
l_seattube = 420
ang_seattube = 76.5
l_reach = 371.9
l_stack = 534
frame = Frame("42", l_seattube, ang_seattube, l_reach, l_stack)
cc.add_frame(frame)
cc.draw()
exit(1)
print("size 48")
l_seattube = 480
ang_seattube = 75
l_reach = 372
l_stack = 534
calc_slope(l_seattube, ang_seattube, l_reach, l_stack)
print("size 51")
l_seattube = 510
ang_seattube = 75
l_reach = 375.4
l_stack = 558.5
calc_slope(l_seattube, ang_seattube, l_reach, l_stack)
print("size 56")
l_seattube = 560
ang_seattube = 73.5
l_reach = 383.1
l_stack = 579.5
calc_slope(l_seattube, ang_seattube, l_reach, l_stack)

draw()
