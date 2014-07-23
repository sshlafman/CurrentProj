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
    def __init__(self, fileName, mode='text', fileMode='read'):
        if not fileName:
            raise ValueError
        if (mode != 'text') and (mode != 'binary'):
            raise ValueError
        if (fileMode != 'read') and (fileMode != 'write') and \
             (fileMode != 'readwrite'):
            raise ValueError
        self.fileName = fileName
        self.mode = mode
        self.fileMode = fileMode
        self._fileHandle = None
        
    def open(self):
        if self.fileMode == 'read':
            mode = 'r'
        elif self.fileMode == 'write':
            mode = 'w'
        elif self.fileMode == 'readwrite':
            mode = 'r+'
        self._fileHandle = open(self.fileName, mode)
    
    def close(self):
        self._fileHandle.close() 
        
    def is_readable(self):
        if self._fileHandle is not None:
            return self._fileHandle.readable()
        return False

    def is_writable(self):
        if self._fileHandle is not None:
            return self._fileHandle.writable()
        return False

    def is_closed(self):
        if self._fileHandle is not None:
            return self._fileHandle.closed
        return False  
