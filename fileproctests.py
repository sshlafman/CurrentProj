import unittest
from fileproc import TextConverter

class TextConverterDefaultTargetEncodingToTestCase(unittest.TestCase):
    def runTest(self):
        """Check that TextConverter is created with default target encoding"""
        converter = TextConverter('866')
        self.assertEqual(converter.targetEncoding, 'utf8', 'incorrect default target encoding') 
        
class TextConverterNoSourceEncodingExceptionTestCase(unittest.TestCase):
    def runTest(self):
        """Check that TextConverter throws exception if no source encoding passed to cnstr"""
        try:
            TextConverter('')
        except ValueError:
            pass
        else:
            self.fail("expected exception ValueError")

class TextConverterInvalidSourceEncodingRaisesExceptionTestCase(unittest.TestCase):
    def runTest(self):
        """Check that TextConverter throws correct exception if source encoding is invalid"""
        try:
            TextConverter('someencoding', 'utf8')
        except LookupError:
            pass
        else:
            self.fail("expected exception LookupError")

class TextConverterInvalidTargetEncodingRaisesExceptionTestCase(unittest.TestCase):
    def runTest(self):
        """Check that TextConverter throws correct exception if target encoding is invalid"""
        try:
            TextConverter('utf8', 'someencoding')
        except LookupError:
            pass
        else:
            self.fail("expected exception LookupError")

class TextConverterInvalidEncodingsRaiseExceptionTestCase(unittest.TestCase):
    def runTest(self):
        """Check that TextConverter throws correct exception if both encodings are invalid"""
        try:
            TextConverter('someencoding', 'anotherencoding')
        except LookupError:
            pass
        else:
            self.fail("expected exception LookupError")

class TextConverterValidateArgumentEncodingsTestCase(unittest.TestCase):
    def runTest(self):
        """Check that TextConverter is created with correct encodings"""
        sourceEncoding = '866'
        targetEncoding = 'utf16'
        converter = TextConverter(sourceEncoding, targetEncoding)
        self.assertEqual(converter.encodings(), (sourceEncoding, targetEncoding), 
                         'incorrect source encoding')
        
class TextConverterInputTextIsBytesStringTestCase(unittest.TestCase):
    def runTest(self):
        """Check that text passed to convert() is a bytes string"""
        converter = TextConverter('866', 'utf16')
        text = 'regular string'
        self.assertRaises(ValueError, converter.convert, text)
        
class TextConverterValidateCorrectConvertionTestCase(unittest.TestCase):
    def runTest(self):
        """Check that conversion is correct"""
        sourceEncoding = '866'
        targetEncoding = 'utf16'
        testText = 'Летят утки'
        
        converter = TextConverter(sourceEncoding, targetEncoding)
        inBytes = bytes(testText, encoding=sourceEncoding)
        outBytes = converter.convert(inBytes)
        self.assertEqual(outBytes.decode(targetEncoding), testText, 'incorrect output in convert()')          
        
if __name__ == "__main__":
    unittest.main()