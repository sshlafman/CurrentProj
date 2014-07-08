import unittest
from fileproc import TextEncoder

class TextEncoderDefaultTargetEncodingToTestCase(unittest.TestCase):
    def runTest(self):
        """Check that TextEncoder is created with default target encoding"""
        encoder = TextEncoder()
        self.assertEqual(encoder.targetEncoding(), 'utf8', 'incorrect default target encoding') 
        
if __name__ == "__main__":
    unittest.main()