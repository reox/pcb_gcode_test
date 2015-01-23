# create lines of length 10mm
# space them in groups with feedrate in 100mm/min steps
from numpy import arange

z_target = -0.04
length = 10.0
spacing = 2.0
plungerate = 100.0

start_feed = 100.0
target_feed = 2000.0


print("G21      ; use mm")
print("G90      ; absolute coordinates")
print("G54      ; use G54 coordinate system")
print("G40      ; turn radius compensation off")
print("G17      ; choose x,y plane")
print("G80      ; Cancel Motion Modes")
print("G94      ; movement speed is in mm/min")
print("G49      ; turn cutter legth compensation off")
print("G0 Z10   ; Go to saftyplane")
print("M3       ; turn on spindle")
print("S24000   ; 6000 min-1 spindle speed")

print("G0 Z10")
print("G0 X0 Y0")
print("G4 P10")

for i, feedrate in enumerate(arange(start_feed, target_feed+1, 100)):
    print("; Feedrate: %f" % (feedrate))
    print("; f_z: %f " % (feedrate / (24000.0*2.0)))
    print("G0 X%f Y0" % (i * spacing))
    # extra wait
    print("G4 P5")
    print("G0 Z2")
    print("F%f" % (plungerate))
    print("G1 Z%f" % (z_target))
    print("F%f" % (feedrate))
    print("G1 Y%f" % (length))
    print("G0 Z10")
    print("")

print("M30")
