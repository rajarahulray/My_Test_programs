# -*- coding: utf-8 -*-

from collections import Counter
from matplotlib import style, pyplot
import warnings
import numpy as np

style.use('fivethirtyeight');

dataset = {'k' : [[1,2], [2,3], [4,2]], 'r' : [[5,3],[3,4],[6,4]]};
new_feature = [2.5,3.5];
def k_nearest(data, predict_data, k = 3):
  if len(data) >= k:
      warnings.warn('k is less than the no. of voting groups!');
  
  distance = [];
  for group in data:
      for features in data[group]:
          euclid_distance = np.linalg.norm(np.array(features) - np.array(predict_data));
          distance.append([euclid_distance, group]);
                          
  votes = [i[1] for i in sorted(distance)[:k]]
  print(Counter(votes).most_common(1));
  vote_result = Counter(votes).most_common(1)[0][0];
  print(vote_result);
  return vote_result;

result = k_nearest(dataset, new_feature, k = 3);
print(result);

[[pyplot.scatter(j[0], j[1], s = 100, color = i)for j in dataset[i]]for i in dataset];
pyplot.scatter(new_feature[0], new_feature[1], color = result);
pyplot.show();
                                      