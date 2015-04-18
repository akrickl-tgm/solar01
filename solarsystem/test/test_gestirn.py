from unittest import TestCase
from solarsystem.Gestirn import *

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

    def test_rotateNeg1(self):
        self.assertRaises(TypeError, self.testobjekt.rotate([-2, 1, 2]))

    def test_rotateNeg1(self):
        self.assertRaises(TypeError, self.testobjekt.rotate([0, -1, 2]))

    def test_rotateNeg1(self):
        self.assertRaises(TypeError, self.testobjekt.rotate([0, 4, -2]))

    def test_rotateFalseType(self):
        self.assertRaises(TypeError, self.testobjekt.rotate("test"))

    def test_translate(self):
        test1 = False
        old = self.testobjekt.position[2]

        self.testobjekt.translate([0, 0, 0.07])

        if self.testobjekt.position[2] == old + 0.07:
            test1 = True

        self.assertTrue(test1, "")

    def test_translateNeg0(self):
        self.assertRaises(TypeError, self.testobjekt.translate([-1, 0, 2]))

    def test_translateNeg1(self):
        self.assertRaises(TypeError, self.testobjekt.translate([0, -3, 2]))

    def test_translateNeg2(self):
        self.assertRaises(TypeError, self.testobjekt.translate([1, 4, -2]))

    def test_translateFalseType(self):
        self.assertRaises(TypeError, self.testobjekt.translate(True))

    def test_setAnimationF(self):
        self.testobjekt.setAnimation(False)
        self.assertFalse(self.testobjekt.anim, "")

    def test_setAnimationT(self):
        self.testobjekt.setAnimation(True)
        self.assertTrue(self.testobjekt.anim, "")

    def test_setAbstand(self):

        self.testobjekt.setAbstand(5)
        self.testobjekt.setAbstand(100)

        self.assertEqual(self.testobjekt.entf_rotPoint, 100)

    def test_setAbstandNeg(self):
        self.assertRaises(TypeError, self.testobjekt.setAbstand(-10))


    def test_isInArea(self):
        self.assertTrue(self.testobjekt.isInArea(1000, 1000, 1000), "")