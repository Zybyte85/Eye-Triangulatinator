import math

def type_check(m1, m2):
    if "/execute" in m1 and m2:
        print("Using execute method")
        return get_from_execute(m1, m2)
    else:
        print("Using XZA method")
        return get_from_XZA(m1, m2)

def get_from_execute(m1, m2):
    split = m1.split()
    split2 = m2.split()
    return(calculate(float(split[6]), float(split[8]), float(split[9]), float(split2[6]), float(split2[8]), float(split2[9])))

def get_from_XZA(m1, m2):
      split = m1.split()
      split2 = m2.split()
      return(calculate(float(split[0]), float(split[1]), float(split[2]), float(split2[0]), float(split2[1]), float(split2[2])))



def mca2deg(mca):
	if mca < -90: 
		return abs(mca) - 90
	elif mca < 0: 
		return 270 + mca
	else:
		return 270 - mca

# Math stuff I definetly understand and I totally didn't copy paste.
def calculate(x1, z1, a1, x2, z2, a2):
    # determine point from casting angle
    x1n = 0+x1+500*math.cos(math.radians(mca2deg(a1)))
    z1n = 0+z1-500*math.sin(math.radians(mca2deg(a1)))
    x2n = 0+x2+500*math.cos(math.radians(mca2deg(a2)))
    z2n = 0+z2-500*math.sin(math.radians(mca2deg(a2)))

    d = ((z2n - z2) * (x1n - x1)) - ((x2n - x2) * (z1n - z1))
    a = z1 - z2
    b = x1 - x2
    n1 = ((x2n - x2) * a) - ((z2n - z2) * b)
    n2 = ((x1n - x1) * a) - ((z1n - z1) * b)
    a = n1 / d
    b = n2 / d
    int_x = x1 + (a * (x1n - x1))
    int_z = z1 + (a * (z1n - z1))

    return(round(int_x), round(int_z), round(math.dist((int_x, int_z), (x1, z1))))
#print(type_check("/execute in minecraft:overworld run tp @s 531.56 70.00 226.64 -140.03 -31.41", "/execute in minecraft:overworld run tp @s 682.35 70.00 260.40 215.23 -31.41"))