__author__ = 'Astrid Krickl'
from OpenGL.GL import *
from OpenGL.GLU import *
from astrid.Texturen import *


class Gestirn:
    def __init__(self):
        pass

    def DrawGLScene_P(self, radius, rot, light, x, y, z, txt):

        glLoadIdentity()                  # Screen neu laden
        # Position des Planeten im Raum
        glTranslatef(x, y, z)             # Positionieren am Screen (x,y,z)

        glRotatef(rot[0], 1.0, 0.0, 0.0)  # Rotatation um X-Achse
        glRotatef(rot[1], 0.0, 1.0, 0.0)  # Rotatation um Y-Achse
        glRotatef(rot[2], 0.0, 0.0, 1.0)  # Rotatation um Z-Achse

        # Entfernung vom Fixstern. dh auf dieser Bahn bewegt sich dann der Planet
        # Mithilfe der setAbstand-Methode setzen
        glTranslatef(2.0, 0, 2.0)       # neu Positionieren am Screen (x,y,z)

        glEnable(GL_LIGHTING)             # Licht an
        """
        if light:
            glEnable(GL_LIGHTING)
        else:
            glDisable(GL_LIGHTING)
        """

        # Planet erstellen
        """
        t = Texturen()
        if txt == 0:
            qua = t.LoadTextures_Sonne()
        else:
            qua = t.LoadTextures_Jupiter()
            """

        gluSphere(txt, radius, 32, 32)  # Parameter: Radius; Longitude; Latitude Segments

    def rotation(self, rot, x, y, z):
        #Rotation um die Sonne
        rot[0] = rot[0] + x  # X achse
        rot[1] = rot[1] + y  # Y achse
        rot[2] = rot[2] + z  # Z achse

        return rot