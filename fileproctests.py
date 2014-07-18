import unittest
from fileproc import TextConverter

class TextConverterCheckForInvalidArgumentsTestCase(unittest.TestCase):
    def test_invalid_arguments_raise_exception(self):
        """Check that TextConverter throws correct exception if both encodings are invalid"""
        try:
            TextConverter('someencoding', 'anotherencoding')
        except LookupError:
            pass
        else:
            self.fail("expected exception LookupError")
            
    def test_invalid_target_encoding_raises_exception(self):
        """Check that TextConverter throws correct exception if target encoding is invalid"""
        try:
            TextConverter('utf8', 'someencoding')
        except LookupError:
            pass
        else:
            self.fail("expected exception LookupError")
        
    def test_invalid_source_encoding_raises_exception(self):
        """Check that TextConverter throws correct exception if source encoding is invalid"""
        try:
            TextConverter('someencoding', 'utf8')
        except LookupError:
            pass
        else:
            self.fail("expected exception LookupError")
    
    def test_no_source_encoding_raises_exception(self):
        """Check that TextConverter throws exception if no source encoding passed to constructor"""
        try:
            TextConverter('')
        except ValueError:
            pass
        else:
            self.fail("expected exception ValueError")

class TextConverterDefaultTargetEncodingToTestCase(unittest.TestCase):
    def runTest(self):
        """Check that TextConverter is created with default target encoding"""
        converter = TextConverter('866')
        self.assertEqual(converter.targetEncoding, 'utf8', 'incorrect default target encoding') 

class TextConverterConversionTestCase(unittest.TestCase):
    def setUp(self):
        self.sourceEncoding = '866'
        self.targetEncoding = 'utf16'
        self.converter = TextConverter(self.sourceEncoding, self.targetEncoding)
              
    def test_validate_arguments(self):
        """Check that TextConverter is created with correct encodings"""
        self.assertEqual(self.converter.encodings(), 
                         (self.sourceEncoding, self.targetEncoding), 
                         'incorrect source encoding')
    
    def test_convert_accepts_bytes_string(self):
        """Check that text passed to convert() is a bytes string"""
        text = 'regular string'
        self.assertRaises(ValueError, self.converter.convert, text)
    
    def test_convert_produces_correct_output(self):        
        """Check that conversion is correct"""
        testText = 'Летят утки'        
        inBytes = bytes(testText, encoding=self.sourceEncoding)
        outBytes = self.converter.convert(inBytes)
        self.assertEqual(outBytes.decode(self.targetEncoding), testText, 'incorrect output in convert()')          
        
if __name__ == "__main__":
    unittest.main()