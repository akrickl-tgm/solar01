__author__ = 'Astrid Krickl, Daniel Herczeg'

from solarsystem.Gestirn import *
from solarsystem.Texturen import *
from solarsystem.Light import *
from solarsystem.Fixstern import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from solarsystem.Planet import *

ESCAPE = '\033'


class Galaxie():

    def __init__(self):
        # Da das Licht von open GL in Objektkoordinaten angezeigt (als Punkt) angezeigt wird,
        # muessen hier die Koordinaten uebergeben werden. Dazu nehme ich einfach den Nullpunkt
        # und verschiebe das Licht 80 Einheiten nach hinten. OpenGL behandelt die z-Achse negativ
        # dh ueberall, wo ich etwas nach hinten schieben moechte, muss ich (nur beim Licht) den pos.
        # Z-Wert hinschreiben.
        # Der zweite Parameter gibt die Lichtfarbe an. In diesem Fall ein leicht gruenliches
        # Licht mit 100 Prozent Alpha
        self.light = Light([0, 0, 0, 80], [0.8, 1.0, 0.8, 1.0])
        self.pos = False  # Kameraansicht
        self.mod = True  # modus texturen an oder aus
        self.lights = True
        self.anim = True
        self.zoom = 0

        # Die ganzen Objektattribute hier leer initialisieren, einfach, weil das
        # die korrekte Python Sprachsyntax besagt.
        self.erdenTextur = None
        self.jupiterTextur = None
        self.marsTextur = None
        self.merkurTextur = None
        self.mondTextur = None
        self.neptunTextur = None
        self.plutoTextur = None
        self.saturnTextur = None
        self.sonnenTextur = None
        self.uranusTextur = None
        self.venusTextur = None
        self.asteroidTextur = None

    def loadTextures(self):
        self.erdenTextur = Texturen.LoadTexture("../data/erde.jpg")
        self.jupiterTextur = Texturen.LoadTexture("../data/jupiter.jpg")
        self.marsTextur = Texturen.LoadTexture("../data/mars.jpg")
        self.merkurTextur = Texturen.LoadTexture("../data/merkur.jpg")
        self.mondTextur = Texturen.LoadTexture("../data/mond.jpg")
        self.neptunTextur = Texturen.LoadTexture("../data/neptun.jpg")
        self.plutoTextur = Texturen.LoadTexture("../data/pluto.jpg")
        self.saturnTextur = Texturen.LoadTexture("../data/saturn.jpg")
        self.sonnenTextur = Texturen.LoadTexture("../data/sonne.jpg")
        self.uranusTextur = Texturen.LoadTexture("../data/uranus.jpg")
        self.venusTextur = Texturen.LoadTexture("../data/venus.jpg")
        self.asteroidTextur = Texturen.LoadTexture("../data/asteroid.jpg")

    def pauseAll(self):
        self.sonne.setAnimation(False)

    def playAll(self):
        self.sonne.setAnimation(True)

    def loadPlanets(self):
        # Parameter(Planet): (position, anim, rotation, rotSpeed, rotPoint, movSpeed, radius, textur, divisions, monde)
        # Parameter(Fixstern): (position, rotSpeed, textur, planeten, anim, licht, radius, divisions)
        # Parameter(Mond): (anim, rotation, rotSpeed, parent, entf_rotPoint, movSpeed, radius, textur, divisions)
        # Fixstern
        self.sonne = Fixstern([0, 0, -80], 0.2, self.sonnenTextur, None, True, self.light, 10, 64)

        # Planeten
        self.merkur = Planet([-17, 0, -80], True, [90, 0, 0], 0.05, self.sonne.position, 0.0001, 0.4, self.merkurTextur, 32, None)
        self.venus = Planet([-20.5, 0, -80], True, [90, 0, 0], 0.05, self.sonne.position, 0.000125, 1.21, self.venusTextur, 32, None)
        self.erde = Planet([-29, 0, -80], True, [90, 0, 0], 1.5, self.sonne.position, 0.0006, 1.28, self.erdenTextur, 32, None)
        self.mars = Planet([-36.5, 0, -80], True, [90, 0, 0], 0.05, self.sonne.position, 0.0009, 0.6, self.marsTextur, 32, None)
        self.jupiter = Planet([-59, 0, -80], True, [90, 0, 0], 0.05, self.sonne.position, 0.00035, 14.3, self.jupiterTextur, 32, None)
        self.saturn = Planet([-85, 0, -80], True, [90, 0, 0], 0.05, self.sonne.position, 0.00056, 12.05, self.saturnTextur, 32, None)
        self.uranus = Planet([-98, 0, -80], True, [90, 0, 0], 0.05, self.sonne.position, 0.0004, 5.11, self.uranusTextur, 32, None)
        self.neptun = Planet([-115, 0, -80], True, [90, 0, 0], 0.05, self.sonne.position, 0.00087, 4.95, self.neptunTextur, 32, None)
        self.pluto = Planet([-125, 0, -80], True, [90, 0, 0], 0.05, self.sonne.position, 0.00025, 0.1, self.plutoTextur, 32, None)

        # Monde
        self.mond = Mond(True, [-90, 0, -80], 0, self.erde, 5, -0.0005, 0.4, self.mondTextur, 24)

        self.erde.addMond(self.mond)
        self.sonne.addPlanet(self.erde)
        self.sonne.addPlanet(self.jupiter)
        self.sonne.addPlanet(self.mars)
        self.sonne.addPlanet(self.merkur)
        self.sonne.addPlanet(self.neptun)
        self.sonne.addPlanet(self.pluto)
        self.sonne.addPlanet(self.saturn)
        self.sonne.addPlanet(self.uranus)
        self.sonne.addPlanet(self.venus)

    def enableTextures(self):
        glEnable(GL_TEXTURE_2D)

    def disableTextures(self):
        glDisable(GL_TEXTURE_2D)

    def init(self, Width, Height):
        glClearColor(0.0, 0.0, 0.0, 0.0)    # Hintergrundfarbe
        glClearDepth(1.0)                   # Loeschen des Depth Buffers
        glDepthFunc(GL_LESS)                # The Type Of Depth Test To Do
        glEnable(GL_DEPTH_TEST)             # Enables Depth Testing
        glShadeModel(GL_SMOOTH)             # Enables Smooth Color Shading

        glMatrixMode(GL_PROJECTION)         # Reset The Projection Matrix
        glLoadIdentity()

        # Calculate The Aspect Ratio Of The Window
        gluPerspective(45.0, float(Width) / float(Height), 0.1, 100000.0)
        glMatrixMode(GL_MODELVIEW)

        glutKeyboardFunc(self.keyPressed)  # steuerung ueber die tatstatur aktivieren

        # Licht initialisieren
        self.light.init()
        self.loadTextures()
        self.loadPlanets()
        self.enableTextures()

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
        gluPerspective(50.0, float(Width) / float(Height), 0.1, 100000.0)  # Naehe
        glMatrixMode(GL_MODELVIEW)
    """
    szene zeichenn
    """
    def DrawGLScene(self):
        self.update()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Screen loeschen und depth buffer loeschen

        self.sonne.draw(self.pos, self.zoom)

        glutSwapBuffers()  # zeichnen

    def update(self):
        self.sonne.update()

    def keyPressed(self, *args):
        if args[0] == b'p':
            if self.anim:
                self.pauseAll()
                self.anim = False
            else:
                self.playAll()
                self.anim = True

        if args[0] == b'c':
            if self.pos:
                self.zoom = 0
                self.pos = False
            else:
                self.zoom = 0
                self.pos = True

        if args[0] == b't':
            if self.mod:
                self.disableTextures()
                self.mod = False
            else:
                self.enableTextures()
                self.mod = True

        if args[0] == b'l':
            if self.lights:
                self.sonne.disableLight()
                self.lights = False
            else:
                self.sonne.enableLight()
                self.lights = True

        if args[0] == b'w':
            self.sonne.animateAllChildrenFaster(0.05, 0.0001)

        if args[0] == b's':
            self.sonne.animateAllChildrenSlower(0.05, 0.0001)

        if args[0] == b'+':
            self.zoom += 5

        if args[0] == b'-':
            self.zoom -= 5