"""Unit tests for the graph.py module.

"""


import unittest

from graphslam.graph import Graph


class TestGraph(unittest.TestCase):
    """Tests for the ``Graph`` class.

    """

    def test_optimize(self):
        """Test that a ``Graph`` can be optimized.

        """
        g = Graph()
        g.optimize()
        self.assertIsNotNone(g)


if __name__ == '__main__':
    unittest.main()