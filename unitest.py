import unittest
import complexvectors
import math


class unit_calculadora(unittest.TestCase):

    def test_sum(self):

        self.assertEqual(complexvectors.sum_comps((5, 20), (15, -7)), (20, 13))

    def test_rest(self):

        self.assertEqual(complexvectors.res_comp((5, 20), (15, -7)), (-10, 27))

    def test_mult(self):

        self.assertEqual(complexvectors.mult_comp((5, 20), (15, -7)), (215, 265))

    def test_div(self):

        self.assertEqual(complexvectors.div_comp((5, 20), (15, -7)), (-0.23722627737226276, 1.2226277372262773))

    def test_mod(self):

        self.assertEqual(complexvectors.mod_comp((-4, 3)), 5)

    def test_conj(self):

        self.assertEqual(complexvectors.conj_comp((-15, -10)), (15, 10))

    def test_polar_cart(self):

        self.assertEqual(complexvectors.polar_cart((math.sqrt(2), (math.pi*3)/4)), (-1.0, 1.0))

    def test_cart_polar(self):

        self.assertEqual(complexvectors.cart_polar((-1.0, 1.0)), (math.sqrt(2), 135.0))

    def test_fase(self):

        self.assertEqual(complexvectors.c_fase((6, 15)), 68.19859051364818)

    def test_suma_vectores(self):
        self.assertEqual(complexvectors.sum_vect([9+7j, 11+0j, 14-18j], [6+3j, 3+1j, 10-8j]),
                         [(15+10j), (14+1j), (24-26j)])

    def test_vector_inverso(self):
        self.assertEqual(complexvectors.inv_vect([9+7j, -4j, 14-18j]), [(-9-7j), 4j, (-14+18j)])

    def test_vectorxescalar(self):
        self.assertEqual(complexvectors.vect_escalar([(-9-7j), (-11+0j), (-14+18j)], 4), [(-36-28j), (-44+0j), (-56+72j)])

    def test_suma_matriz(self):
        self.assertEqual(complexvectors.sum_matrix_comp([[4+8j, 7+1j, 8+4j], [4j, 6j, 7-8j]],
                                                         [[6+3j, 3+1j, 10-8j], [-8j, 4+10j, 2-1j]]),
                         [[(10+11j), (10+2j), (18-4j)], [-4j, (4+16j), (9-9j)]])

    def test_matriz_inversa(self):
        self.assertEqual(complexvectors.inv_matrix([[4+8j, 7+1j, 8+4j], [4j, 6j, 7-8j]]),
                         [[(-4-8j), (-7-1j), (-8-4j)], [(-0-4j), (-0-6j), (-7+8j)]])

    def test_matrizxescalar(self):
        self.assertEqual(complexvectors.matrix_escalar([[6+3j, 3+1j, 10-8j], [-8j, 4+10j, 2-1j]], 4),
                         [[(24+12j), (12+4j), (40-32j)], [-32j, (16+40j), (8-4j)]])

    def test_transpuesta(self):
        self.assertEqual(complexvectors.trans([[4+8j, 7+1j, 8+4j], [4j, 6j, 7-8j]]),
                         [[(4+8j), 4j], [(7+1j), 6j], [(8+4j), (7-8j)]])

    def test_conjugar(self):
        self.assertEqual(complexvectors.conjg([[4+8j, 7+1j, 8+4j], [4j, 6j, 7-8j]]),
                         [[(4-8j), (7-1j), (8-4j)], [-4j, -6j, (7+8j)]])

    def test_adjunta(self):
        self.assertEqual(complexvectors.matrix_adj([[4+8j, 7+1j, 8+4j], [4j, 6j, 7-8j]]),
                         [[(4-8j), -4j], [(7-1j), -6j], [(8-4j), (7+8j)]])

    def test_multiplicacion(self):
        self.assertEqual(complexvectors.matrix_matrix([[4+8j, 4j, 8-3j], [7+1j, 6j, 4+5j], [8+4j, 7-8j, 10]],
                                                 [[6+3j, -8j, 5], [3+1j, 4+10j, 9j], [10-8j, 2-1j, 10+4.5j]]),
                         [[(52-22j), (37-30j), (77.5+46j)], [(113+63j), (-39-26j), (-1.5+73j)], [(165-49j), (160-36j),
                                                                                                 (212+128j)]])

    def test_productointerno(self):
        self.assertEqual(complexvectors.prod_int_vect([4+8j, 4j, 8-3j], [8+4j, 7-8j, 10]), (112-46j))

    def test_norma_vector(self):
        self.assertEqual(complexvectors.norma([(4, 5), (3, 1), (0, -7)]), 10.0)

    def test_distancia(self):
        self.assertEqual(complexvectors.distancia_vecotres([(3, 8), (5, -2), (8, -10)], [(8, 9), (3, -7), (6, 14)]),
                         25.199206336708304)

    def test_hermitania(self):
        self.assertEqual(complexvectors.hermitian([[(3+0j),(2-1j),(-3j)],[(2+1j),(0+0j),(1-1j)],[(0+3j),(1+1j),(0+0j)]]),True)

if __name__ == '__main__':
    unittest.main()
