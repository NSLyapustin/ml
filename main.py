import pygame
import numpy as np

def dist(pntA, pntB):
    return np.sqrt((pntA[0] - pntB[0]) ** 2 + (pntA[1] - pntB[1]) ** 2)

def bfs(current_point, points, marked_points):
    for point in points:
        if dist(current_point, point)

def dbscan(points):
    minPts = 3
    eps = 100
    flags = list(np.zeros(len(points)))
    # green
    for i in range(len(points)):
        numberPts = 0
        for j in range(len(points)):
            if dist(points[i], points[j])<eps and i != j:
                numberPts += 1
        if numberPts > minPts:
            flags[i] = 'green'
    # yellow
    for i in range(len(points)):
        if flags[i] == 0:
            for j in range(len(points)):
                if flags[j] == 'green' and dist(points[i], points[j])<eps:
                    flags[i] = 'yellow'

    # red
    for i in range(len(points)):
        if flags[i] == 0:
            flags[i] = 'red'
    print(flags)
    return flags


def paint():
    points = []
    x, y = [], []
    R = 7
    pygame.init()
    screen = pygame.display.set_mode([800, 600])
    screen.fill(color='white')
    pygame.display.update()
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    points.append(event.pos)
                    pygame.draw.circle(screen, color='black', center=event.pos, radius=R)
                    pygame.display.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    flags = dbscan(points)
                    for i in range(len(points)):
                        pygame.draw.circle(screen, color=flags[i], center=points[i], radius=R)
        pygame.display.update()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    paint()
