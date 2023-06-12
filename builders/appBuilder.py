from helpers.constants import AppTypes


class AppBuilder:
    def Build(self, types: AppTypes):
        match types:
            case AppTypes.BotApplication:
                self.__build_bot()
                pass
            case AppTypes.RestApplication:
                self.__build_rest_api()
                pass

    def __build_rest_api(self):
        pass

    def __build_bot(self):
        pass
