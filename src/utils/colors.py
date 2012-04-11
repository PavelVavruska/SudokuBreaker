__author__ = '@PavelVavruska'


class bcolors:
    """
       Colored console output
       """
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'
    BOLD = "\033[1m"

    @staticmethod
    def printOK(string):
        print bcolors.OKGREEN + string + bcolors.ENDC,

    @staticmethod
    def printOK_BOLD(string):
        print bcolors.BOLD + bcolors.OKGREEN + string + bcolors.ENDC,

    @staticmethod
    def printWarning(string):
        print bcolors.WARNING + string + bcolors.ENDC,

    @staticmethod
    def printWarning_BOLD(string):
        print bcolors.BOLD + bcolors.WARNING + string + bcolors.ENDC,

    @staticmethod
    def printError(string):
        print bcolors.ERROR + string + bcolors.ENDC,
