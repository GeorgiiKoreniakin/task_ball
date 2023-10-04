import math



def degree(t: float, a: float, r: float, v: float = 0) -> float:
    # Calculating the angular displacement using the formula S = V0 * t + (a*t**2)/2
    S = v * t + (a * t ** 2) / 2
    
    # Calculate the circumference using the formula C = 2*pi*r
    C = 2 * math.pi * r
    
    # Calculate the angle in radians by dividing the displacement by the circumference
    radians = S / C
    
    # Convert the angle from radians to degrees
    print(radians)
    print(round(radians))
    degrees = 360 * abs(math.floor(radians) - radians)
    
    return round(degrees, 2)

result = degree(5, 3, 10)
print(result)



