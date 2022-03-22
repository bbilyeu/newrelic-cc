#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test case to ensure functionality."""

import unittest
import pep8
from bbilyeu import ThreeWordSequenceSeeker

# This route was taken over trying to cover the minutiae of stdin on
# multiple operating systems in a relatively short timeframe.
TEST_STDIN = [
    "“What do you think of that now, Flask? ain’t there a small drop of something queer about that, eh? A white whale—did ye mark that, man? Look ye—there’s something special in the wind. Stand by for it, Flask. Ahab has that that’s bloody on his mind. But, mum; he comes this way.”",
    "“All ye mast-headers have before now heard me give orders about a white whale. Look ye! d’ye see this Spanish ounce of gold?”—holding up a broad bright coin to the sun—“it is a sixteen dollar piece, men. D’ye see it? Mr. Starbuck, hand me yon top-maul.”",
    "Receiving the top-maul from Starbuck, he advanced towards the main-mast with the hammer uplifted in one hand, exhibiting the gold with the other, and with a high raised voice exclaiming: “Whosoever of ye raises me a white-headed whale with a wrinkled brow and a crooked jaw; whosoever of ye raises me that white-headed whale, with three holes punctured in his starboard fluke—look ye, whosoever of ye raises me that same white whale, he shall have this gold ounce, my boys!”",
    "“It’s a white whale, I say,” resumed Ahab, as he threw down the topmaul: “a white whale. Skin your eyes for him, men; look sharp for white water; if ye see but a bubble, sing out.”",
    "“Captain Ahab,” said Tashtego, “that white whale must be the same that some call Moby Dick.”"
]

class TestSeeker(unittest.TestCase):
    """Test ThreeWordSequenceSeeker to ensure requirements are met."""

    def test_stdin_result_count(self):
        """Verify that 100 results are returned."""
        seeker = ThreeWordSequenceSeeker()
        seeker.stdin_data = TEST_STDIN
        seeker.run(print_output=False)
        self.longMessage = True
        self.assertEqual(len(seeker.results), 100, 'unexpected number of results')
    
    def test_stdin_result_contents(self):
        """Verify the second result."""
        seeker = ThreeWordSequenceSeeker()
        seeker.stdin_data = TEST_STDIN
        seeker.run(print_output=False)
        self.longMessage = True
        self.assertEqual(seeker.results[1][0], 'whosoever of ye', 'mismatch on second three-word sequence')

    def test_file_result_count(self):
        """Verify that 100 results are returned."""
        seeker = ThreeWordSequenceSeeker()
        seeker.possible_files = ['moby-dick.txt']
        seeker.run(print_output=False)
        self.longMessage = True
        self.assertEqual(len(seeker.results), 100, 'unexpected number of results')
    
    def test_file_result_contents(self):
        """Verify the third result."""
        seeker = ThreeWordSequenceSeeker()
        seeker.possible_files = ['moby-dick.txt']
        seeker.run(print_output=False)
        self.longMessage = True
        self.assertEqual(seeker.results[2][0], 'the white whale', 'mismatch on third three-word sequence')

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./bbilyeu/__init__.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()