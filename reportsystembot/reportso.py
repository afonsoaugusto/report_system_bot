import platform

class ReportSO:

    def __init__(self):
        pass

    def getArch(self):
        return platform.architecture()[0]

    #def getTop
