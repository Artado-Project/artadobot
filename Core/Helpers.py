from zope.interface import interface, implementer


class IHelper(interface):
    pass


@implementer(IHelper)
class ILoggerHelper(interface):
    pass


@implementer(IHelper)
class IConfigurator(interface):
    def MigrateConfiguration(self):
        pass
