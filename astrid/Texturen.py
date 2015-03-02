__author__ = 'Astrid Krickl'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL.Image import *      # fuer texturen


class Texturen():

    def LoadTexture(self, pic):

        if pic == "jupiter":
            # Bild auswaehlen
            image = open("./jupiter.jpg")
        elif pic == "sonne":
            image = open("./lava.jpg")

        # Textur
        ix = image.size[0]
        iy = image.size[1]
        image = image.tostring("raw", "RGBX", 0, -1)

        # Textur erstellen
        textures = glGenTextures(3)
        glBindTexture(GL_TEXTURE_2D, int(textures[0]))  # 2d texture (x and y size)

        # Planet P1
        glBindTexture(GL_TEXTURE_2D, int(textures[2]))
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
        gluBuild2DMipmaps(GL_TEXTURE_2D, 3, ix, iy, GL_RGBA, GL_UNSIGNED_BYTE, image)

        planet1 = gluNewQuadric()
        gluQuadricNormals(planet1, GLU_SMOOTH)  # Create Smooth Normals (NEW)
        gluQuadricTexture(planet1, GL_TRUE)  # Create Texture Coords (NEW)

        return planet1
