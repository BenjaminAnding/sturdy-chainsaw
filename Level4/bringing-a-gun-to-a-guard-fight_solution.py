import math
def mirror_atlas(node, dimensions, distance):
    node_mirrored = []
    for i in range(len(node)):
        points = []
        for j in range(-(distance//dimensions[i])-1, (distance//dimensions[i])+2):
            points.append(get_mirror(j, node[i], dimensions[i]))
        node_mirrored.append(points)
    return node_mirrored


def get_mirror(nth_reflection, coordinate, dimension):
    result = coordinate
    distances_from_walls = [2*coordinate, 2*(dimension-coordinate)]
    if(nth_reflection < 0):
        for i in range(nth_reflection, 0):
            result -= distances_from_walls[(i+1) % 2]
    else:
        for i in range(nth_reflection, 0, -1):
            result += distances_from_walls[i % 2]
    return result


def solution(dimensions, your_position, guard_position, distance):
    mirrored = [mirror_atlas(your_position, dimensions, distance), mirror_atlas(guard_position, dimensions, distance)]
    result = set()
    angles_dist = {}
    for i in range(0, len(mirrored)):
        for j in mirrored[i][0]:
            for k in mirrored[i][1]:
                angle = math.atan2((your_position[1]-k), (your_position[0]-j))
                dist = math.sqrt((your_position[0]-j)**2 + (your_position[1]-k)**2)
                if distance >= dist:
                    if((angle in angles_dist and angles_dist[angle] > dist) or angle not in angles_dist):
                        angles_dist[angle] = dist
                        if i > 0:
                            result.add(angle)
    return len(result)
print(solution([3,2], [1,1], [2,1], 4))
print(solution([300,275], [150,150], [185,100], 500))
