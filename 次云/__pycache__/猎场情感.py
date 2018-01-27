import importlib
import sys
importlib.reload(sys)

import numpy as np
from snownlp import SnowNLP
import matplotlib.pyplot as plt

comment = []
with open('comments.txt', mode='r') as f:
    rows = f.readlines()
    for row in rows:
        if row not in comment:
            comment.append(row.strip('\n'))


def snowanalysis(self):
    sentimentslist = []
    for li in self:
        s = SnowNLP(li)
        print(li)
        print(s.sentiments)
        sentimentslist.append(s.sentiments)
    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01))
    plt.show()


if __name__ == '__main__':
    snowanalysis(comment)

