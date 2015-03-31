__author__ = 'thor'

from misc.analysis_dashboard.two_tag_analyzer import TwoTagAnalyzer

analyzer_info = dict()

analyzer_info['test_analyzer'] = {
    'constructor': TwoTagAnalyzer,
}

analyzer_info['two_tag_analyzer'] = {
    'constructor': TwoTagAnalyzer,
    'arguments': dict(mgcol='salmund_5s_fv',
                      mgdb='sound',
                      feat_field='fv',
                      tag_field='token',
                      tag_1='car',
                      tag_2='bird')
}
