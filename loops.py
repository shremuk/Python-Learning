# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 21:45:43 2018

@author: DELL
"""

(a, b) = (2, 3)
a
a, b = b, a
b



mer = pd.DataFrame(np.arange(9).reshape(3,3), index = ['A','B','C'], columns = list('abc'))
mer
mer1 = pd.DataFrame(np.arange(9).reshape(3,3), index = ['M','N','O'], columns = list('amn'))
mer1
mer1 = mer.merge(mer1, on = 'a')
mer1
