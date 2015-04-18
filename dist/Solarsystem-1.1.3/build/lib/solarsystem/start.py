__author__ = 'Astrid Krickl, Daniel Herczeg'

import sys
from solarsystem.splashscreen import *
import tkinter
from solarsystem.Galaxie import *

width = 1000
height = 600

def main(sc):
        """
        # splashscreen
        tkRoot = tkinter.Tk()
        s = Splash(tkRoot, '../data/splash.gif', 2.0)
        s.__enter__()
        s.__exit__()

        # basis fenster schließen
        tkRoot.withdraw()
        """

        #solarsystem
        glutInit(sys.argv)

        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)   # Select type of Display mode
        glutInitWindowSize(width, height)                               # get a 640 x 480 window
        glutInitWindowPosition(50, 50)                              # the window starts at the upper left corner of the screen
        glutCreateWindow(b'Solarsystem')                            # Titel
        glutDisplayFunc(sc.DrawGLScene)                           # Register the drawing function with glut
        glutIdleFunc(sc.DrawGLScene)                              # scene nochmal zeichnen
        glutReshapeFunc(sc.ReSizeGLScene)                         # fenstergroesse aendern
        sc.init(640, 480)                                       # fenster initialisieren
        glutMainLoop()


s = Galaxie(width, height)
main(s)