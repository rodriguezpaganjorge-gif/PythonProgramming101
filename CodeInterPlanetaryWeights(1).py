# Author: Jorge Rodriguez 
# Class: Python Programming - CIT-115-D02
## Purpose: calculate a person’s weight on the different planets within our solar system by multiplying their mass by the gravity factor on the surface of the planet.

MERCURY_GRAVITY = 0.38
VENUS_GRAVITY = 0.91
MOON_GRAVITY = 0.165
MARS_GRAVITY = 0.38
JUPITER_GRAVITY = 2.34
SATURN_GRAVITY = 0.93
URANUS_GRAVITY = 0.92
NEPTUNE_GRAVITY = 1.12
PLUTO_GRAVITY = 0.066

s_Name = input("Enter your name: ")
s_InputWeight = input("Enter your Earthling weight (i.e 150.0): ")
f_EarthWeight = float(s_InputWeight)

f_MercuryWeight = f_EarthWeight * MERCURY_GRAVITY
f_VenusWeight = f_EarthWeight * VENUS_GRAVITY
f_MoonWeight = f_EarthWeight * MOON_GRAVITY
f_MarsWeight = f_EarthWeight * MARS_GRAVITY
f_JupiterWeight = f_EarthWeight * JUPITER_GRAVITY
f_SaturnWeight = f_EarthWeight * SATURN_GRAVITY
f_UranusWeight = f_EarthWeight * URANUS_GRAVITY
f_NeptuneWeight = f_EarthWeight * NEPTUNE_GRAVITY
f_PlutoWeight = f_EarthWeight * PLUTO_GRAVITY

print()
print(f"{s_Name}'s Solar System's Weights")
print("-" * 36)
print(f"{'Mercury:':<12}{f_MercuryWeight:>10.2f}")
print(f"{'Venus:':<12}{f_VenusWeight:>10.2f}")
print(f"{'Moon:':<12}{f_MoonWeight:>10.2f}")
print(f"{'Mars:':<12}{f_MarsWeight:>10.2f}")
print(f"{'Jupiter:':<12}{f_JupiterWeight:>10.2f}")
print(f"{'Saturn:':<12}{f_SaturnWeight:>10.2f}")
print(f"{'Uranus:':<12}{f_UranusWeight:>10.2f}")
print(f"{'Neptune:':<12}{f_NeptuneWeight:>10.2f}")
print(f"{'Pluto:':<12}{f_PlutoWeight:>10.2f}")
