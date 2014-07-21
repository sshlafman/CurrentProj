class TextConverter:
    """Encodes text into another encoding"""
    def __init__(self, sourceEncoding, targetEncoding='utf8'):
        self.validateEncoding(sourceEncoding)
        self.validateEncoding(targetEncoding)
        self.sourceEncoding = sourceEncoding    
        self.targetEncoding = targetEncoding
        
    def validateEncoding(self, encoding):
        import codecs
        if not encoding:
            raise ValueError
        else:
            codecs.lookup(encoding)
    
    def encodings(self):
        return (self.sourceEncoding, self.targetEncoding)
            
    def convert(self, bytesString):
        if not isinstance(bytesString, bytes):
            raise ValueError
        return bytesString.decode(self.sourceEncoding).encode(self.targetEncoding)

class FileStream:
    def __init__(self, fileName, mode):
        if not fileName:
            raise ValueError
        if (mode != 'text') or (mode != 'binary'):
            raise ValueError
        self.fileName = fileName
        self.mode = mode
        
                