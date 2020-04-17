import yaml
class SecretData():
    def __init__(self):
        f = open('secrets.yml')
        self._data = yaml.load(f.read(), Loader=yaml.CBaseLoader)
    def getValue(self,key):
        return self._data[key]
