from _datetime import datetime


class TerminalHelper:
    @staticmethod
    def printCyan(skk): print("\033[96m {}\033[00m".format(skk))

    @staticmethod
    def printPurple(skk): print("\033[95m {}\033[00m".format(skk))

    @staticmethod
    def printYellow(skk): print("\033[93m {}\033[00m".format(skk))

    @staticmethod
    def printRed(skk): print("\033[91m {}\033[00m".format(skk))

    @staticmethod
    def printGreen(skk): print("\033[92m {}\033[00m".format(skk))

    @staticmethod
    def inputCyan(skk): return input("\033[96m {}\033[00m".format(skk))

    @staticmethod
    def inputPurple(skk): return input("\033[95m {}\033[00m".format(skk))

    @staticmethod
    def inputRed(skk): return input("\033[91m {}\033[00m".format(skk))

    @staticmethod
    def inputGreen(skk): return input("\033[92m {}\033[00m".format(skk))


class LoggerHelper:

    def Info(self, message: str | object):
        date = f"[{datetime.now()}]"
        log_type = "[INFO]"
        log = f"{date} {log_type} [{message}]"
        TerminalHelper.printGreen(log)
        pass

    def Warning(self, message: str | object):
        date = f"[{datetime.now()}]"
        log_type = "[WARNING]"
        log = f"{date} {log_type} [{message}]"
        TerminalHelper.printYellow(log)
        pass

    def Error(self, message: str | object):
        date = f"[{datetime.now()}]"
        log_type = "[ERROR]"
        log = f"{date} {log_type} [{message}]"
        TerminalHelper.printRed(log)
        pass

    pass
