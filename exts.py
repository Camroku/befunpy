from importlib import import_module


class Extensions:
    def __init__(self):
        self.extensions = []

    def registerall(self, regfunc, reglist):
        for ext in self.extensions:
            extension = import_module("extensions." + ext)
            extension.register(regfunc, reglist)

    def registerext(self, extension):
        self.extensions += [extension]


extsi = Extensions()

# Import extensions here
extsi.registerext("reverse")
