import unittest
from fileproc import TextConverter, FileStream

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
        
class FileStreamCheckForInvalidArgumentsTestCase(unittest.TestCase):
    def test_validate_file_name_is_not_empty(self):
        """Check that FileStream throws exception if no fileName passed to constructor"""
        try:
            FileStream('', 'text', 'read')
        except ValueError:
            pass
        else:
            self.fail("expected exception ValueError")
            
    def test_default_mode (self):
        """Check that FileStream's mode is set by default to 'text'"""
        expectedMode = 'text'
        file = FileStream('anyfile')
        self.assertEqual(file.mode, expectedMode, 'Not %s mode by default' % expectedMode)
            
    def test_validate_mode (self):
        """Check that FileStream throws exception if mode is neither 'text' nor 'binary'"""
        try:
            FileStream('anyfile', 'anymode', 'read')
        except ValueError:
            pass
        else:
            self.fail("expected exception ValueError")
            
    def test_default_file_mode (self):
        "Check that FileStream's file mode is set by default to 'read'"
        expectedFileMode = 'read'
        file = FileStream('anyfile')
        self.assertEqual(file.fileMode, expectedFileMode, 'Not %s file mode by default' % expectedFileMode)
        
    def test_validate_file_mode (self):
        "Check that FileStream throws exception if file mode is neither of 'read/write/readwrite'"
        try:
            FileStream('anyfile', mode='text', fileMode='uknownFileMode')
        except ValueError:
            pass
        else:
            self.fail("expected exception ValueError")
        
    def test_setting_explicit_arguments (self):
        """Check that arguments of FileStream's Cstr are set correctly"""
        expectedName = 'anyfile'
        expectedMode = 'text'
        expectedFileMode = 'write'
        file = FileStream(expectedName, expectedMode, expectedFileMode)
        self.assertEqual(file.fileMode, expectedFileMode, 'Wrong file mode')
        self.assertEqual(file.mode, expectedMode, 'Wrong mode')
        self.assertEqual(file.fileName, expectedName, 'Wrong file name')
         
class FileStreamCheckOpenFileTestCase(unittest.TestCase):
    def setUp(self):
        import tempfile
        tmpFile = tempfile.NamedTemporaryFile(delete=False)
        self.fileStream = FileStream(tmpFile.name)
        tmpFile.close()
         
    def tearDown(self):
        self.fileStream.close()

    def test_open_stream(self):
        'Check that stream is opened'
        self.fileStream.open()
        self.assertFalse(self.fileStream.is_closed(), 'File is not opened')
        

    def test_open_read_text_file(self):
        'Check that file is opened correctly in read mode'
        self.fileStream.mode = 'text'
        self.fileStream.fileMode = 'read'
        self.fileStream.open()
        self.assertTrue(self.fileStream.is_readable(), 'file is not readable')
        self.assertFalse(self.fileStream.is_writable(), 'file is writable')

    def test_open_write_text_file(self):
        'Check that file is opened correctly in write mode'
        self.fileStream.mode='text'
        self.fileStream.fileMode='write'
        self.fileStream.open()
        self.assertTrue(self.fileStream.is_writable(), 'file is not writable')
        self.assertFalse(self.fileStream.is_readable(), 'file is readable')
        
    def test_open_read_write_text_file(self):
        'Check that file is opened correctly in read-write mode'
        self.fileStream.mode='text'
        self.fileStream.fileMode='readwrite'
        self.fileStream.open()
        self.assertTrue(self.fileStream.is_writable(), 'file is not writable')
        self.assertTrue(self.fileStream.is_readable(), 'file is not readable')
                
    def test_close_stream(self):
        'Check that file is closed after closing stream'
        self.fileStream.open()
        self.fileStream.close()
        self.assertTrue(self.fileStream.is_closed(), 'File is not closed')
        
if __name__ == "__main__":
    unittest.main()
    