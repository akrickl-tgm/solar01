__author__ = 'Astrid Krickl'

from astrid import Gestirn
from astrid.Texturen import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

ESCAPE = '\033'


class universe():

    def __init__(self):
        self.rot_pl1 = [0, 0, 0]        # sonne
        self.rot_pl2 = [0, 0, 0]        # Planet P1
        self.rot_pl3 = [0, 0, 0]        # Planet P2
        self.rot_pl4 = [0, 0, 0]        # Mond

        #licht
        self.light = 0
        # texturen
        self.quadratic = None
        self.quadratic_p1 = None

    """
    setup für opengl
    """
    def InitGL(self, Width, Height):
        t = Texturen()
        self.quadratic = t.LoadTexture("jupiter")
        self.quadratic_p1 = t.LoadTexture("sonne")

        glEnable(GL_TEXTURE_2D)
        glClearColor(0.0, 0.0, 0.0, 0.0)    # Hintergrundfarbe
        glClearDepth(1.0)                   # Loeschen des Depth Buffers
        glDepthFunc(GL_LESS)                # The Type Of Depth Test To Do
        glEnable(GL_DEPTH_TEST)             # Enables Depth Testing
        glShadeModel(GL_SMOOTH)             # Enables Smooth Color Shading

        glMatrixMode(GL_PROJECTION)         # Reset The Projection Matrix
        glLoadIdentity()

        # Calculate The Aspect Ratio Of The Window
        gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

        # Lichter
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.5, 0.5, 0.5, 1.0))  # Ambient Light
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))  # Diffuse Light
        glLightfv(GL_LIGHT0, GL_POSITION, (0.0, 0.0, 2.0, 1.0)) # Position The Light
        glEnable(GL_LIGHT0)

    """
    Wenn die groesse vom Fenster geaendert wird
    """
    def ReSizeGLScene(self, Width, Height):

        # Wenn das Fenster zu klein ist, erhoehen auf 1
        if Height == 0:
            Height = 1

        glViewport(0, 0, Width, Height)  # Reset The Current Viewport And Perspective Transformation
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        # Perspektive
        gluPerspective(50.0, float(Width) / float(Height), 0.1, 100.0)  # Naehe
        glMatrixMode(GL_MODELVIEW)


    """
    szene zeichenn
    """
    def DrawGLScene(self):

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Screen loeschen und depth buffer loeschen

        # Sonne
        Gestirn.DrawGLScene_P(1, self.rot_pl1, self.light, -1, 0, -12, self.quadratic)

        # Planet P1
        self.rot_pl2 = Gestirn.rotation(self.rot_pl2, 0, 0.04, 0)                           # Rotation
        Gestirn.DrawGLScene_P(0.5, self.rot_pl2, self.light, 0.8, 0, -10, self.quadratic)
        # Radius; rotation koord, light, x,y,z, textur x- 0 sonne - 1 jupiterx

        # Planet P2
        self.rot_pl3 = Gestirn.rotation(self.rot_pl3, 0, 0.02, 0)                           # Rotation
        Gestirn.DrawGLScene_P(0.5, self.rot_pl3, self.light, 3, 0, -10, self.quadratic_p1)

        # Mond
        self.rot_pl4 = Gestirn.rotation(self.rot_pl4, 0.0, 0.03, 0.0)                        # Rotation
        Gestirn.DrawGLScene_P(0.2, self.rot_pl4, self.light, 0, 0, -10, self.quadratic)

        glutSwapBuffers()  # zeichnen



