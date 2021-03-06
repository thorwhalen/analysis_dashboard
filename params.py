__author__ = 'thor'

from ut.wserv.dashboard.test_analyzer import TestAnalyzer

# from two_tag_analyzer import TwoTagAnalyzer

default = dict()
default['save_fig_params'] = {'save_format': 'png', 'dpi': 80, 'bbox_inches': 'tight', 'pad_inches': 0.4}

analyzer_info = dict()

analyzer_info['test_analyzer'] = {
    'constructor': TestAnalyzer
}

# analyzer_info['two_tag_analyzer'] = {
#     'constructor': TwoTagAnalyzer,
#     'arguments': dict(mgcol='salmund_5s_fv',
#                       mgdb='sound',
#                       feat_field='fv',
#                       tag_field='token',
#                       tag_1='car',
#                       tag_2='bird')
# }
