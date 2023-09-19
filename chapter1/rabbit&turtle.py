print("*** Rabbit & Turtle ***")
d, Vr, Vt, Vf = input("Enter Input : ").split()
delta_vtr = float(Vt) - float(Vr)
time = float(d) / delta_vtr
distance_fly = float(Vf)*time
print("%.2f" %distance_fly)