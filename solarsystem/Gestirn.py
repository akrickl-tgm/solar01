__author__ = 'Astrid Krickl, Daniel Herczeg'
from OpenGL.GL import *
from OpenGL.GLU import *
from solarsystem.Texturen import *


class Gestirn:
    def __init__(self, position, anim, rotation, rotSpeed, rotPoint, entf_rotPoint, movSpeed, radius, textur, divisions):
        self.position = position  # Position im XYZ-Raum
        self.anim = anim  # Animationen an/aus
        self.rotation = rotation  # Rotation um die eigene Achse
        self.rotSpeed = rotSpeed  # Rotationsgeschwindigkeit
        self.rotPoint = rotPoint  # Punkt, um den sich der Planet bewegen soll
        self.entf_rotPoint = entf_rotPoint  # Entfernung von ebendiesem Punkt
        self.movSpeed = movSpeed  # Orbitalgeschwindigkeit
        self.radius = radius  # Radius des Himmelskoerpers
        self.textur = textur  # Textur
        self.divisions = divisions  # Unterteilungen. Mehr = feinere, schoenere Kugel
        self.top = False

    def init(self):
        pass

    def update(self):
        # Beim update einfach immer den Himmelskoerper um seine eigene achste rotieren
        if self.anim:
            # Nur dann, wenn die animation nicht pausiert wurde
            self.rotate([0, 0, self.rotSpeed])

    def draw(self, top, zoom):
        # Identity-Matrix neu laden
        glLoadIdentity()

        # Je nachdem, welchen Sichtmodus der User gewaehlt hat, wird die Kamera
        # an einer anderen Stelle gezeichnet bzw. zeigt auf einen anderen Punkt
        if top:
            # Ansicht von oben
            gluLookAt(0, 100-zoom, 0, 0, 0, -80, 0, 1, 0)
        else:
            # Seitenansicht
            gluLookAt(0, 0, 10-zoom, 0, 0, -80, 0, 1, 0)

        # Den Himmelskoerper auf seine Position bewegen, bevor er rotiert
        # wird. Aendert man die Reihenfolge der Transformationen, aendert
        # sich auch das Ergebnis. Zuerst drehen, dann bewegen ->
        # Bewegung evtl falsch, daher zuerst bewegen, dann drehen
        glTranslatef(self.position[0], self.position[1], self.position[2])

        # Objekt um die eigene Achse drehen
        glRotatef(self.rotation[0], 1.0, 0.0, 0.0)  # Rotatation um X-Achse
        glRotatef(self.rotation[1], 0.0, 1.0, 0.0)  # Rotatation um Y-Achse
        glRotatef(self.rotation[2], 0.0, 0.0, 1.0)  # Rotatation um Z-Achse

        # Die Textur zuweisen
        glBindTexture(GL_TEXTURE_2D, self.textur)
        quadratic = gluNewQuadric()
        gluQuadricNormals(quadratic, GLU_SMOOTH)
        gluQuadricTexture(quadratic, GL_TRUE)

        # Zeichnet eine Kugel auf den Bildschirm
        gluSphere(quadratic, self.radius, self.divisions, self.divisions)

    def rotate(self, rotation):
        # Nur wenn das Array drei werte hat, weitermachen
        if len(rotation) == 3:
            self.rotation[0] += rotation[0]
            self.rotation[1] += rotation[1]
            self.rotation[2] += rotation[2]

        # TODO: Werte auf Sinnhaftigkeit pruefen

    def translate(self, pos):
        if len(pos) == 3:
            # Nur wenn das Array drei werte hat, weitermachen
            self.position[0] += pos[0]
            self.position[1] += pos[1]
            self.position[2] += pos[2]

        # TODO: Werte auf Sinnhaftigkeit pruefen

    def setAnimation(self, anim):
        if isinstance(anim, bool):
            self.anim = anim

    def setAbstand(self, abstand):
        # Nur wenn der Abstand numerisch ist, weitermachen
        if isinstance(abstand, int) or isinstance(abstand, float):
            self.entf_rotPoint = abstand