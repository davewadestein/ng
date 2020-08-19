class MyDefaultDict(dict):
    mapper = { int: 0, str: '', list: [] }

    def __init__(self, type):
        self.dict = {}
        if type in self.mapper:
            self.default = self.mapper[type]
        else:
            raise TypeError(f'Unknown default dict type: {type}')
           
    def __getitem__(self, key):
        return self.get(key)

    def get(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            return self.default
