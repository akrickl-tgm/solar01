__author__ = 'Daniel Herczeg'

from solarsystem.Gestirn import *

class Asteroid(Gestirn):
    def __init__(self, position, dir, speed, rotSpeed, anim, radius, textur, divisions):
        """
        Konstruktor fuer einen Asteroid
        :param position: pos des asteroids
        :param dir: richtiung
        :param speed: geschwindigkeit
        :param rotSpeed: rotationsgeschwindigkeit
        :param anim: animation
        :param radius: radius
        :param textur: textur
        :param divisions:
        :return:
        """
        self.position = position  # Position im XYZ-Raum
        self.direction = dir  # Die Richtung, in der der Asteroid fliegen soll
        self.anim = anim  # Animationen an/aus
        self.rotation = [0, 0, 0]  # Rotation um die eigene Achse
        self.rotSpeed = rotSpeed  # Rotationsgeschwindigkeit
        self.speed = speed  # Fluggeschwindigkeit
        self.radius = radius  # Radius des Himmelskoerpers
        self.textur = textur  # Textur
        self.divisions = divisions  # Unterteilungen. Mehr = feinere, schoenere Kugel
        self.top = False
        self.valid = True

    def update(self):
        """
        update methode des asteroids
        :return:
        """
        if self.isInArea(2000, 2000, 2000):
            Gestirn.update(self)

            # Den Asteroiden in jedem Durchlauf verschieben
            self.position[0] = self.position[0] + self.direction[0] * self.speed
            self.position[1] = self.position[1] + self.direction[1] * self.speed
            self.position[2] = self.position[2] + self.direction[2] * self.speed
        else:
            # Wenn er ausserhalb der definierten Grenzen ist, wird
            # er ungueltig und kann von einer anderen Stelle aus geloescht werden.
            self.valid = False

    def draw(self, top, zoom):
        """
        zeichnet einen Asteroiden
        :param top:
        :param zoom:
        :return:
        """
        if self.isInArea(2000, 2000, 2000):
            # Nur zeichnen, wenn der Asteroid in den bestimmten Grenzen ist.
            Gestirn.draw(self, top, zoom)