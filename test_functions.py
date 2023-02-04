import unittest
import A_Teddy_Bear_Picnic
import base_convert
import Generating_Permutations
class test_functions(unittest.TestCase):
    def test_A_Teddy_Bear_Picnic(self):
        self.assertEqual(A_Teddy_Bear_Picnic.bears(250), True)
        self.assertEqual(A_Teddy_Bear_Picnic.bears(42), True)
        self.assertEqual(A_Teddy_Bear_Picnic.bears(53), False)
        self.assertEqual(A_Teddy_Bear_Picnic.bears(41), False)
    def test_base_convert(self):
        self.assertEqual(base_convert.convert(30, 4), "132")
        self.assertEqual(base_convert.convert(45, 2), "101101")
        self.assertEqual(base_convert.convert(316, 16), "13C")
    def test_Generating_Permutations(self):
        self.assertEqual(Generating_Permutations.perm_gen_lex("abc"), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])