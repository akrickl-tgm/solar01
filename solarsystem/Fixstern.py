__author__ = 'Daniel'

from solarsystem.Gestirn import *
from solarsystem.Light import *


class Fixstern(Gestirn):
    def __init__(self, position, rotSpeed, textur, planeten, anim, licht, radius, divisions):
        self.position = position  # Position im XYZ-Raum
        self.anim = anim  # Animationen an/aus
        self.textur = textur  # Textur
        self.divisions = divisions  # Unterteilungen. Mehr = feinere, schoenere Kugel
        self.licht = licht
        self.radius = radius
        self.rotation = [0, 90, 0]
        self.rotSpeed = rotSpeed
        self.inialSpeeds = [rotSpeed]

        if isinstance(planeten, list):
            self.planeten = planeten
        else:
            self.planeten = []

    def addPlanet(self, planet):
        self.planeten.append(planet)

    def getPlanetAt(self, index):
        return self.planeten[index]

    def getPlaneten(self):
        return self.planeten

    def setAnimation(self, anim):
        self.anim = anim

        for x in range(0, len(self.planeten)):
            self.planeten[x].setAnimation(anim)

    def draw(self, top, zoom):
        Gestirn.draw(self, top, zoom)

        if isinstance(self.licht, Light):
            self.licht.draw()

        for x in range(0, len(self.planeten)):
            if isinstance(self.planeten[x], Gestirn):
                self.planeten[x].draw(top, zoom)

    def update(self):
        if self.anim:
            Gestirn.update(self)

        for x in range(0, len(self.planeten)):
            self.planeten[x].update()

    def animateAllChildrenFaster(self, factor, factorMov):
        self.rotSpeed += factor

        for i in range(0, len(self.planeten)):
            self.planeten[i].animateAllChildrenFaster(factor, factorMov)

    def animateAllChildrenSlower(self, factor, factorMov):
        if self.rotSpeed - factor > self.inialSpeeds[0]:
            self.rotSpeed -= factor
        else:
            self.rotSpeed = self.inialSpeeds[0]

        for i in range(0, len(self.planeten)):
            self.planeten[i].animateAllChildrenSlower(factor, factorMov)

    def disableLight(self):
        self.licht.disable()

    def enableLight(self):
        self.licht.enable()