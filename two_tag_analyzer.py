__author__ = 'thor'

import pandas as pd
import numpy as np
from pymongo import MongoClient

from ut.daf.diagnosis import diag_df


class TwoTagAnalyzer(object):
    def __init__(self,
                 mgcol='salmund_5s_fv',
                 mgdb='sound',
                 feat_field='fv',
                 tag_field='tokens',
                 tag_1='car',
                 tag_2='bird'):
        self.mgc = MongoClient()[mgdb][mgcol]
        self.feat_field = feat_field
        self.tag_field = tag_field

        self.tag_1 = tag_1
        self.tag_2 = tag_2
        self.set_tags(tag_1=tag_1, tag_2=tag_2)

        self.all_features = self.mgc.find_one(fields=[self.feat_field])[self.feat_field].keys()
        self.current_features = []
        self.set_current_features()

        self.d = pd.DataFrame()

    def set_tags(self, tag_1='car', tag_2='bird'):
        d = pd.DataFrame([x[self.feat_field] for x in self.mgc.find({self.tag_field: tag_1}, fields=[self.feat_field])])
        d['tag'] = tag_1
        dd = pd.DataFrame([x[self.feat_field] for x in self.mgc.find({self.tag_field: tag_2}, fields=[self.feat_field])])
        dd['tag'] = tag_2
        ddd = pd.concat([d, dd])
        self.tag_1 = tag_1
        self.tag_2 = tag_2
        self.d = self.data_prep(ddd)

    def set_current_features(self, feature_list=None):
        if feature_list is None:
            feature_list = self.get_random_features()
        self.current_features = feature_list

    def get_random_features(self, num_of_features=5):
        return np.random.choice(self.all_features, num_of_features)

    def get_data_stats(self):
        data_stats = dict()
        data_stats[self.tag_1] = self.d[self.d['tag'] == self.tag_1].describe()
        data_stats[self.tag_2] = self.d[self.d['tag'] == self.tag_2].describe()
        return data_stats

    def data_prep(self, ddd):
        diag = diag_df(ddd)
        print("row/cols before: {}".format(np.shape(ddd)))
        tags = ddd['tag']
        ddd = ddd[diag[diag['num_uniques'] > 1]['column']]
        ddd = ddd[np.array([c for c in ddd.columns if ddd[c].dtype == np.dtype('float64')])]
        self.all_features = list(ddd.columns)
        ddd['tag'] = tags
        # ddd = pd.concat([ddd[['tag']], t])
        print("row/cols after: {}".format(np.shape(ddd)))

        print("before dropping Nans: {} items".format(len(ddd)))
        t = ddd.dropna()
        print("after dropping Nans: {} items".format(len(t)))
        for tok in np.unique(t['tag']):
            print("num of {}: {}".format(tok, sum(t['tag'] == tok)))

        return t