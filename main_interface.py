__author__ = 'thor'




class MainInterface(object):
    def __init(self):
        from misc.analysis_dashboard.params import analyzer_info
        self.analyzer_info = analyzer_info
        self.analyzer = None

    def get_analyzer_list(self):
        return self.analyzer_info.keys()

    def set_analyzer(self, analyzer_name):
        _analyzer = self.analyzer_info[analyzer_name]
        self.analyzer = _analyzer['constructor'](**_analyzer['arguments'])

