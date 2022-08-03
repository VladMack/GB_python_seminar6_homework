def find_farthest_orbit(list_of_orbits):
    max_orbit = (0, 0)
    for i in list_of_orbits:
        if i[0] != i[1] and i[0] * i[1] > max_orbit[0] * max_orbit[1]:
            max_orbit = i
    return max_orbit


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
