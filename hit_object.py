import read_file 

class HitObject():

   
    def __init__(self, column, position, length):
        self._column = HitObject.traducir_column(column)
        self._position = position
        self._length = length

    @property
    def column(self):
        return self._column
    
    @property
    def position(self):
        return self._position
    
    @property
    def length(self):
        return self._length

    def traducir_column(column):
        return 63-(int(column)//(512//int(read_file.KEYMODE)))
