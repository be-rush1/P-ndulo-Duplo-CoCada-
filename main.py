

'''

função pendulo = y''(theta,t) = -(g/l) * sen(theta)
L = energia cinética - energia potencial

L = 1/2*m(x1'(t)^2 + y1'(t)^2 + x2'(t)^2 + y2'(t)^2) + 1/2 * I(theta1'(t)^2 + theta2'(t)^2) - m*g*(y1 + y2)


'''

import pygame
import math
import numpy as np
import time


def imagem(it, g=9.8, l =3):
    amostra = []
    dx = math.pi / it
    ini = 0.0
    for i in range(it):
        amostra.append( - (g/l) * math.sin(ini - i*dx))
    return amostra



def mover_pendulo_simples(theta,l=200):  #l em pixeis, não confundir com l do
    return (640 - l*math.cos(theta)  ,360 - l*math.sin(theta) )



def mover_pendulo_duplo(theta1, theta2):
    R1 = 200
    R2 = 250

    x1 = 640 + R1 * np.sin(theta1)
    y1 = 260 + R1 * np.cos(theta1)

    x2 = x1 + R2 * np.sin(theta2)
    y2 = y1 + R2 * np.cos(theta2)

    pygame.draw.line(screen, "white", (x1,y1), (x2,y2))
    pygame.draw.circle(screen, "white", center=(x2, y2), radius=5)
    pygame.draw.line(screen, "red", (640, 260), (x1, y1))
    pygame.draw.circle(screen, "red", center=(x1, y1), radius=5)

    pygame.display.flip()



def pendulo_duplo(theta1, theta2):

    R1 = .2
    R2 = .3
    m2 = .1
    m1 = .2
    g = 9.8

    thetat1 = 0
    thetat2 = 0



    pygame.draw.line(screen, "white", (640, 760), (640, 960))
    pygame.draw.circle(screen, "white", center=(640, 960), radius=5)
    pygame.draw.line(screen, "red", (640, 560), (640, 760))
    pygame.draw.circle(screen, "red", center=(640, 760), radius=5)

    pygame.display.flip()


    dt = 0.01
    while True:

        screen.fill("black")

        num1 = -g * (2 * m1 + m2) * np.sin(theta1)
        num2 = -m2 * g * np.sin(theta1 - 2 * theta2)
        num3 = -2 * np.sin(theta1 - theta2) * m2
        num4 = thetat1 * theta1 * R2 + thetat1 * theta1 * R1 * np.cos(theta1 - theta2)

        den = R1 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2))
        thetatt1 = (num1 + num2 + num3 * num4) / den

        num5 = 2 * np.sin(theta1 - theta2)
        num6 = (thetat1 ** 2 * R1 * (m1 + m2))
        num7 = g * (m1 + m2) * np.cos(theta1)
        num8 = thetat2 * thetat2 * R2 * m2 * np.cos(theta1 - theta2)
        den = R2 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2))
        thetatt2 = (num5 * (num6 + num7 + num8)) / den


        thetat1 += thetatt1 * dt
        thetat2 += thetatt2 * dt
        theta1 += thetat1 * dt
        theta2 += thetat2 * dt
        mover_pendulo_duplo(theta1,theta2)
        time.sleep(0.01)
    pygame.quit()

def diferença_finita_seg_der(it):
    res = []
    f = imagem(it)
    h = math.pi / it
    for i in range(1,it-2):
        res.append((f[i+1] - 2*f[i] +f[i-1]) / h**2)
    return res

def pendulo_simples(it):
    val = diferença_finita_seg_der(it)
    pygame.draw.line(screen, "white", (640, 360), (640, 560))
    pygame.draw.circle(screen, "white", center=(640, 560), radius=5)
    time.sleep(0.1)
    pygame.draw.circle(screen, "black", center=(640, 560), radius=5)
    for i in val:
        screen.fill("black")
        x2, y2 = mover_pendulo_simples(i)
        pygame.draw.line(screen, "white", (640, 360), (x2, y2))
        pygame.draw.circle(screen, "white", center=(x2, y2), radius=5)
        pygame.display.flip()
        time.sleep(0.1)
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pendulo_duplo(math.pi/3, -4*math.pi/9)
    pygame.quit()
