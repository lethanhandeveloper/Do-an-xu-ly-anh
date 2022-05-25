import numpy as np
from PyQt5 import QtCore
from PyQt5.QtGui import QImage

class Segmentation(QtCore.QThread):
    ImageUpdate = QtCore.pyqtSignal(np.ndarray)
    Dialog=QtCore.pyqtSignal()
    def __init__(self,image, k, iters, isKmean):
        QtCore.QThread.__init__(self,  )
        self.image=image
        self.k=k
        self.iters=iters
        self.isKmean=isKmean
    
        
    def run(self):  # expects img in rgb
        img = self.image.copy()
        self.Dialog.emit()
        if(self.isKmean == True):
            try:
                h, w, c = img.shape
                orig = self.image.copy()
                Klusters = np.random.randint(0, 255, size=(self.k, 3))
                # print('init clusters', Klusters)
                for it in range(self.iters):
                    img = self.image.copy()
                    for i in range(h):
                        for j in range(w):
                            pnt = img[i][j]

                            diff = np.sqrt(np.sum((Klusters - pnt) ** 2, axis=1))
                            # print('clusters', Klusters)
                            # print('PNT', pnt)
                            # print('Diff', diff)
                            c = np.argmin(diff)
                            # print('ARGMIN', c)
                            img[i][j] = Klusters[c]
                    # loss=0
                    l = []
                    for i in range(self.k):
                        Ys, Xs, c = np.where(img == Klusters[i])
                        kth_points = orig[Ys, Xs]
                        l.append(np.sum(Klusters[i] - kth_points))
                        Klusters[i] = np.mean(kth_points, axis=0)
            except:
                    pass
                    # loss=sum(l)
                # print('Cluster centroids at iteration-{}'.format(it+1), Klusters)
                # print('loss at iteration-{}'.format(it+1),loss)
        self.ImageUpdate.emit(img)
       