from zope.interface import implementer
from os import environ

from core.helpers import IConfigurator


@implementer(IConfigurator)
class EnvConfigurator:
    def __init__(self):
        pass

    def MigrateConfiguration(self, env_variable) -> str:
        return environ.get(env_variable)
