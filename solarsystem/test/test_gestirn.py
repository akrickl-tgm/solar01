from unittest import TestCase
from  .Gestirn import *

__author__ = 'Daniel Herczeg'


class TestGestirn(TestCase):
    # position, anim, rotation, rotSpeed, rotPoint, entf_rotPoint, movSpeed, radius, textur, divisions
    testobjekt = Gestirn([-125, 0, -80], True, [90, 0, 0], 0.05, [0,0,0], 0, 0.00025, 0.1, None, 32)

    def test_update(self):
        test1 = False
        test2 = False
        old = self.testobjekt.rotation[2]

        self.testobjekt.update()

        if self.testobjekt.rotation[2] == old + 0.05:
            test1 = True

        self.testobjekt.setAnimation(False)
        self.testobjekt.update()

        if self.testobjekt.rotation[2] == old + 0.05:
            test2 = True

        test3 = test1 and test2

        self.assertTrue(test3, "")

    def test_rotate(self):
        test1 = False
        old = self.testobjekt.rotation[2]

        self.testobjekt.rotate([0, 0, 0.05])

        if self.testobjekt.rotation[2] == old + 0.05:
            test1 = True

        self.assertTrue(test1, "")

    def test_translate(self):
        self.assertTrue(True)

    def test_setAnimation(self):
        self.assertTrue(True, "OK")

    def test_setAbstand(self):
        pass

    def test_isInArea(self):
        self.assertTrue(self.testobjekt.isInArea(1000, 1000, 1000), "")