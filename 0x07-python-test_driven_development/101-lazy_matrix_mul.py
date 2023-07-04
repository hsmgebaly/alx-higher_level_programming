#!/usr/bin/python3
# uses NumPy to define a matrix multiplication function.

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """ Return the results of multiplying two matrices.

    Arguments will be as following:
        m_a (list of lists of ints/floats): The 1st  matrix.
        m_b (list of lists of ints/floats): The 2nd matrix.
    """

    return (np.matmul(m_a, m_b))
