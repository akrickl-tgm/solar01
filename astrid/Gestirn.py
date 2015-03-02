__author__ = 'Astrid Krickl'
from OpenGL.GL import *
from OpenGL.GLU import *
from astrid.Texturen import *


def DrawGLScene_P(radius, rot, light, x, y, z, txt):

    glLoadIdentity()                  # Screen neu laden
    glTranslatef(x, y, z)             # Positionieren am Screen (x,y,z)

    glRotatef(rot[0], 1.0, 0.0, 0.0)  # Rotatation um X-Achse
    glRotatef(rot[1], 0.0, 1.0, 0.0)  # Rotatation um Y-Achse
    glRotatef(rot[2], 0.0, 0.0, 1.0)  # Rotatation um Z-Achse

    glTranslatef(3.0, 0.0, 2.0)       # neu Positionieren am Screen (x,y,z)

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


def rotation(rot, x, y, z):
    #Rotation um die Sonne
    rot[0] = rot[0] + x  # X achse
    rot[1] = rot[1] + y  # Y achse
    rot[2] = rot[2] + z  # Z achse

    return rot


