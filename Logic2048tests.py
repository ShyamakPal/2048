# 2048 Testing


import unittest
from Logic2048 import *

class BoardTests(unittest.TestCase):
    def setUp(self):
        self._game = Logic2048()

    def test_empty_board_creation(self):
        self.assertEqual(self._game.get_board(), [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

    def test_set_board(self):
        board = [[1,50,70,30],[20,40,50,60],[20,40,50,60],[50,90,0,60]]
        self._game.set_board(board)
        self.assertEqual(self._game.get_board(), [[1,50,70,30],[20,40,50,60],[20,40,50,60],[50,90,0,60]])

    def test_empty_spaces(self):
        self.assertEqual(self._game.get_empty(), [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)])
        board = [[1,50,70,30],[20,40,50,60],[20,40,50,60],[50,90,0,60]]
        self._game.set_board(board)
        self.assertEqual(self._game.get_empty(), [(3,2)])

    def test_spawn(self):
        self._game.spawn()
        counts = self._count(self._game.get_board())
        self.assertTrue(counts[2] == 1 or counts[4] == 1)
        self._game.spawn()
        self._game.spawn()
        counts = self._count(self._game.get_board())
        self.assertTrue(counts[2] + counts[4] == 3)

    def _count(self, board: list[list[int]]) -> dict:
        out = dict()
        out[2] = 0
        out[4] = 0
        for i in board:
            for j in i:
                if j in out.keys():
                    out[j] += 1
                else:
                    out[j] = 1
        return out

class MoveTests(unittest.TestCase):
    def setUp(self):
        self._game = Logic2048()

    def test_shift(self):
        out = self._game.shift([0,0,0,0])
        self.assertEqual(out, [0,0,0,0])
        out = self._game.shift([1,0,0,0])
        self.assertEqual(out, [0,0,0,1])
        out = self._game.shift([1,2,0,0])
        self.assertEqual(out, [0,0,1,2])
        out = self._game.shift([1,0,2,0])
        self.assertEqual(out, [0,0,1,2])
        out = self._game.shift([1,2,3,4])
        self.assertEqual(out, [1,2,3,4])
        out = self._game.shift([1,0,0,4])
        self.assertEqual(out, [0,0,1,4])

    def test_match(self):
        out = self._game.match([0,0,0,0])
        self.assertEqual(out, [0,0,0,0])
        out = self._game.match([0,0,1,1])
        self.assertEqual(out, [0,0,0,2])
        out = self._game.match([0,1,2,1])
        self.assertEqual(out, [0,1,2,1])
        out = self._game.match([1,1,2,2])
        self.assertEqual(out, [0,2,0,4])
        out = self._game.match([1,1,3,2])
        self.assertEqual(out, [0,2,3,2])
        out = self._game.match([1,1,1,1])
        self.assertEqual(out, [0,2,0,2])

    def test_process(self):
        out = self._game.process([0,0,0,0])
        self.assertEqual(out, [0,0,0,0])
        out = self._game.process([0,0,1,1])
        self.assertEqual(out, [0,0,0,2])
        out = self._game.process([1,2,1,0])
        self.assertEqual(out, [0,1,2,1])
        out = self._game.process([1,1,2,2])
        self.assertEqual(out, [0,0,2,4])
        out = self._game.process([1,1,0,0])
        self.assertEqual(out, [0,0,0,2])
        out = self._game.process([1,1,1,1])
        self.assertEqual(out, [0,0,2,2])
                         
if __name__ == '__main__':
    unittest.main()
