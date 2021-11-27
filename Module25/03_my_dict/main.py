class MyDict(dict):
    def __init__(self, dict):
        self.dict = dict

    def get(self, key):
        res = dict(self).get(key)
        if res == None:
            return 0
        else:
            return res


dict1 = {1: 1}
dict2 = MyDict(dict1)

print(dict1.get(2))
print(dict2.get(2))
