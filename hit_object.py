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
        if column == 64:
            return 63
        if column == 192 :
            return 62 
        if column == 320 :
            return 61
        if column == 448 :
            return 60
