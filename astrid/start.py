__author__ = 'Astrid Krickl'

from astrid.Solarsys import *
import sys
from astrid.splashscreen import *
import tkinter


def main(sc):
        #splashscreen
        tkRoot = tkinter.Tk()
        s = Splash(tkRoot, '../data/splash.gif', 2.0)
        s.__enter__()
        s.__exit__()

        #solarsystem
        glutInit(sys.argv)

        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)   # Select type of Display mode
        glutInitWindowSize(1000, 600)                               # get a 640 x 480 window
        glutInitWindowPosition(50, 50)                              # the window starts at the upper left corner of the screen
        glutCreateWindow(b'Solarsystem')                            # Titel
        glutDisplayFunc(sc.DrawGLScene)                           # Register the drawing function with glut
        glutIdleFunc(sc.DrawGLScene)                              # scene nochmal zeichnen
        glutReshapeFunc(sc.ReSizeGLScene)                         # fenstergroesse aendern
        #glutKeyboardFunc(self.keyPressed)			                    # Tastertur verwenden
        sc.InitGL(640, 480)                                       # fenster initialisieren
        glutMainLoop()


s = universe()
main(s)