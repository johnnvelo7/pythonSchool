from math import pi
def main ():
    radius = int(input("Enter radius of the sphere: "))
    volume = volume_sphere(radius)
    print(f"Volume of a sphere with radius of {radius} = {volume : .2f}")

def volume_sphere (r):
    volume = (4/3) * pi * r ** 3
    return volume

main()