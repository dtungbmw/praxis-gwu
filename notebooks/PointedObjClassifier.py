from DepthEstimator import *
from ObjectDetector import ObjectDetector
from GesturePointingDirectionEstimator import *
    
class PointedObjectClassifier:
    
    def __init__(self, pointingDirEstimator, objectDetector):
        self.pointingDirEstimator = pointingDirEstimator
        self.objectDetector = objectDetector
    
    def classify(self, video):
        res_class = None
        res_p = 0
        
        return res_class, res_p
    
    
    
    
    
    
    