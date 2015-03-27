__author__ = 'Daniel Herczeg'

from astrid.Gestirn import *
from math import *

class Mond(Gestirn):
    def __init__(self, anim, rotation, rotSpeed, parent, entf_rotPoint, movSpeed, radius, textur, divisions):
        self.anim = anim  # Animationen an/aus
        self.rotation = rotation  # Rotation um die eigene Achse
        self.rotSpeed = rotSpeed  # Rotationsgeschwindigkeit
        self.rotPoint = parent.position  # Punkt, um den sich der Planet bewegen soll
        self.position = [parent.position[0]+entf_rotPoint, parent.position[1], parent.position[2]]
        self.entf_rotPoint = abs(self.rotPoint[0] - self.position[0])  # Entfernung von ebendiesem Punkt
        self.movSpeed = movSpeed  # Orbitalgeschwindigkeit
        self.radius = radius  # Radius des Himmelskoerpers
        self.textur = textur  # Textur
        self.divisions = divisions  # Unterteilungen. Mehr = feinere, schoenere Kugel
        self.orbitalPos = 0
        self.inialSpeeds = [rotSpeed, movSpeed]

    def update(self):
        if self.anim:
            self.orbitalPos += self.movSpeed

            # Eigenes Update Verhalten hier erzeugen (Auf einer Kreisbahn bewegen)
            rads = self.orbitalPos*(180/3.14)

            self.position[0] = self.rotPoint[0] + cos(rads) * self.entf_rotPoint
            self.position[2] = self.rotPoint[2] + sin(rads) * self.entf_rotPoint

    def animateFaster(self, factor, factorMov):
        self.rotSpeed += factor
        self.movSpeed += factorMov

    def animateSlower(self, factor, factorMov):
        if self.rotSpeed - factor > self.inialSpeeds[0]:
            self.rotSpeed -= factor
        else:
            self.rotSpeed = self.inialSpeeds[0]

        if self.movSpeed - factorMov > self.inialSpeeds[1]:
            self.movSpeed -= factorMov
        else:
            self.movSpeed = self.inialSpeeds[1]