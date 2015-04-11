__author__ = 'thor'


from params import analyzer_info


class MainInterface(object):
    """
    Class that is meant to manage the selection of an analyzer.
    """
    def __init__(self, analyzer_info=analyzer_info):
        self.analyzer_info = analyzer_info
        self.analyzer = None

    def get_analyzer_list(self):
        return self.analyzer_info.keys()

    def set_analyzer(self, analyzer_name):
        _analyzer = self.analyzer_info[analyzer_name]
        self.analyzer = _analyzer['constructor']()



