__author__ = 'Astrid Krickl'

from astrid.Gestirn import *
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
        self.gestirn = Gestirn()

        #licht
        self.light = 0
        # texturen
        self.quadratic_sonne = None
        self.quadratic_jupiter = None
        self.quadratic_mond = None
        self.quadratic_mars = None
        self.pos = False
        self.mod = True  # modus texturen an oder aus
    """
    setup für opengl
    """
    def InitGL(self, Width, Height):

        self.quadratic_jupiter = Texturen.LoadTexture("./jupiter.jpg", self.mod)
        self.quadratic_sonne = Texturen.LoadTexture("./sonne.jpg", self.mod)
        self.quadratic_mars = Texturen.LoadTexture("./mars1.jpg", self.mod)
        self.quadratic_mond = Texturen.LoadTexture("./mond1.jpg", self.mod)


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

        glutKeyboardFunc(self.keyPressed)  # steuerung ueber die tatstatur aktivieren

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
        self.gestirn.DrawGLScene_P(1, self.rot_pl1, self.light, -1, 0, -12, self.quadratic_sonne, self.pos)

        # Planet P1
        self.rot_pl2 = self.gestirn.rotation(self.rot_pl2, 0, 0.04, 0)                           # Rotation
        self.gestirn.DrawGLScene_P(0.5, self.rot_pl2, self.light, 0.8, 0, -10, self.quadratic_mars, self.pos)
        # Radius; rotation koord, light, x,y,z, textur x- 0 sonne - 1 jupiterx

        # Planet P2
        self.rot_pl3 = self.gestirn.rotation(self.rot_pl3, 0, 0.02, 0)                           # Rotation
        self.gestirn.DrawGLScene_P(0.5, self.rot_pl3, self.light, 3, 0, -10, self.quadratic_jupiter, self.pos)

        # Mond
        self.rot_pl4 = self.gestirn.rotation(self.rot_pl4, 0.0, 0.03, 0.0)                        # Rotation
        self.gestirn.DrawGLScene_P(0.2, self.rot_pl4, self.light, 0, 0, -10, self.quadratic_mond, self.pos)

        glutSwapBuffers()  # zeichnen

    def changePos(self):
        if self.pos is True:
            self.pos = False
        else:
            self.pos = True

    def changeTextures(self):
        if self.mod is True:
            self.mod = False
        else:
            self.mod = True

        self.quadratic_jupiter = Texturen.LoadTexture("./jupiter.jpg", self.mod)
        self.quadratic_sonne = Texturen.LoadTexture("./sonne.jpg", self.mod)
        self.quadratic_mars = Texturen.LoadTexture("./mars1.jpg", self.mod)
        self.quadratic_mond = Texturen.LoadTexture("./mond1.jpg", self.mod)

    def keyPressed(self, *args):
        if args[0] == b'c':
            self.changePos()

        if args[0] == b't':
            self.changeTextures()


