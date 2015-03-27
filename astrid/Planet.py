__author__ = 'Daniel Herczeg'

from astrid.Gestirn import Gestirn
from astrid.Mond import Mond
from math import *

class Planet(Gestirn):
    def __init__(self, position, anim, rotation, rotSpeed, rotPoint, movSpeed, radius, textur, divisions, monde):
        self.position = position  # Position im XYZ-Raum
        self.anim = anim  # Animationen an/aus
        self.rotation = rotation  # Rotation um die eigene Achse
        self.rotSpeed = rotSpeed  # Rotationsgeschwindigkeit
        self.rotPoint = rotPoint  # Punkt, um den sich der Planet bewegen soll
        self.entf_rotPoint = abs(rotPoint[0] - position[0])  # Entfernung von ebendiesem Punkt
        self.movSpeed = movSpeed  # Orbitalgeschwindigkeit
        self.radius = radius  # Radius des Himmelskoerpers
        self.textur = textur  # Textur
        self.divisions = divisions  # Unterteilungen. Mehr = feinere, schoenere Kugel
        self.orbitalPos = 0  # Wie weit hat sich der Planet auf seiner Kreisbahn bereits bewegt?
        self.inialSpeeds = [rotSpeed, movSpeed]

        if isinstance(monde, list):
            self.monde = monde
        else:
            self.monde = []

    def getMondAt(self, index):
        if 0 <= index < len(self.monde):
            return self.monde[index]
        else:
            return None

    def update(self):
        if self.anim:
            Gestirn.update(self)

            self.orbitalPos += self.movSpeed * 0.2

            # Eigenes Update Verhalten hier erzeugen (Auf einer Kreisbahn bewegen)
            rads = self.orbitalPos*(180/3.14)

            self.position[0] = self.rotPoint[0] + cos(rads) * self.entf_rotPoint
            self.position[2] = self.rotPoint[2] + sin(rads) * self.entf_rotPoint

        for x in range(0, len(self.monde)):
            self.monde[x].update()

    def draw(self, top, zoom):
        Gestirn.draw(self, top, zoom)

        for x in range(0, len(self.monde)):
            self.monde[x].draw(top, zoom)

    def getMonde(self):
        return self.monde

    def addMond(self, m):
        if isinstance(m, Mond):
            self.monde.append(m)

    def createMond(self, rotation, rotSpeed, entf_rotPoint, movSpeed, radius, textur, divisions):
        self.addMond(Mond(self.anim, rotation, rotSpeed, self, entf_rotPoint, movSpeed, radius, textur, divisions))

    def animateAllChildrenFaster(self, factor, factorMov):
        self.rotSpeed += factor
        self.movSpeed += factorMov

        for i in range(0, len(self.monde)):
            self.monde[i].animateFaster(factor, factorMov)


    def animateAllChildrenSlower(self, factor, factorMov):
        if self.rotSpeed - factor > self.inialSpeeds[0]:
            self.rotSpeed -= factor
        else:
            self.rotSpeed = self.inialSpeeds[0]

        if self.movSpeed - factorMov > self.inialSpeeds[1]:
            self.movSpeed -= factorMov
        else:
            self.movSpeed = self.inialSpeeds[1]

        for i in range(0, len(self.monde)):
            self.monde[i].animateSlower(factor, factorMov)

    def setAnimation(self, anim):
        Gestirn.setAnimation(self, anim)

        for i in range(0, len(self.monde)):
            self.monde[i].setAnimation(anim)