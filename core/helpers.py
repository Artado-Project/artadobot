from zope.interface import Interface, implementer


class IHelper(Interface):
    pass


@implementer(IHelper)
class ILoggerHelper(Interface):
    pass


@implementer(IHelper)
class IConfigurator(Interface):
    def MigrateConfiguration(self, env_variable) -> str:
        pass
