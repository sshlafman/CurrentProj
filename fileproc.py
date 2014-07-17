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
        #text.decode
                