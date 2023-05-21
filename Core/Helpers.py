from zope.interface import interface, implementer


class IHelper(interface):
    def Help(self):
        pass


@implementer(IHelper)
class ILoggerHelper(interface):
    pass


@implementer(IHelper)
class IConfigurator(interface):
    pass
