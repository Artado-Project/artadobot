from zope.interface import interface


class IBuilder(interface):
    def Build(self):
        pass
