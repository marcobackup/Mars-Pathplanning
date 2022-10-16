import matplotlib.pyplot as plt
import math
import sys


plt.title('Mars pathplanning')
plt.axis([-1000, 1000, -1000, 1000])
plt.imshow(
    plt.imread('mars-pathplanning/bg.jpeg'), extent=[-1000, 1000, -1000, 1000], aspect='auto'
)

coordinates = []
with open('mars-pathplanning/points.txt', 'r') as points:
    for point in points.readlines()[1:]:
        point = point.split(',')
        coordinates.append(
            [float(point[0].strip()), float(point[1].strip())]
        )

startPoint = coordinates[0]

for coordinate in coordinates:
    if coordinates.index(coordinate) == 0:
        marker = 'X'
        color = 'green'
    else:
        marker = 'o'
        color = 'red'
    plt.scatter(coordinate[0], coordinate[1], color=color, marker=marker)
    plt.pause(0.3)

# calculate shortest path
lastPoint = 0
c1, c2, = None, None
paths = []
for _ in range(len(coordinates)):
    _ = lastPoint
    min = sys.float_info.max
    for i in range(len(coordinates)):
        dist = math.hypot(coordinates[i][0] - coordinates[_][0], coordinates[i][1] - coordinates[_][1])
        if dist > 0 and dist < min:
            min = dist
            c1 = coordinates[_]
            c2 = coordinates[i]
    if len(coordinates) <= 1:
        paths.append([c2, startPoint, math.hypot(coordinates[i][0] - startPoint[0], coordinates[i][1] - startPoint[1])])
        break
    paths.append([c1, c2, min])
    coordinates.remove(c1)
    lastPoint = coordinates.index(c2)

# draw lines and calculate total distance traveled
totalMeters = 0
for path in paths:
    plt.plot([path[0][0], path[1][0]], [path[0][1], path[1][1]], color='red')
    totalMeters += path[2]
    plt.pause(0.1)

"""
    paths: [[x1, y1], [x2, y2], distance]
"""
print(paths)
print(f'total distance: {round(totalMeters, 1)}m')
plt.title(f'Mars pathplanning - total distance: {round(totalMeters, 1)}m')

plt.show()

