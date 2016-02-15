import time

class CameraSpecs:
    def __init__(self, maxRes, minRes, nSteps, desiredFPS, ratio = (4.0 / 3.0)):
        self.maxResolution = maxRes
        self.minResolution = minRes
        self.nSteps = nSteps
        self.ratio = ratio
        
        self.prevCheck = time.time()
        self.resolutionIndex = nSteps - 1
        
        self.resolution = self.getResolution(self.resolutionIndex)
        #self.resolution = self.getResolution(0)
        self.framerate = desiredFPS
        self.frameTimes = []
        self.FPS = 0
        self.margin = 5
        
    def checkChange(self):
        if time.time() - self.prevCheck < 5.0: return False
        self.prevCheck = time.time()
        
        diff = self.FPS - self.framerate
        if diff < -self.margin and self.resolutionIndex > 0:
            self.resolutionIndex -= 1
            self.resolution = self.getResolution(self.resolutionIndex)
            return True
        elif diff > self.margin and self.resolutionIndex < self.nSteps-1:
            self.resolutionIndex += 1
            self.resolution = self.getResolution(self.resolutionIndex)
            return True
        return False
    
    def getResolution(self, i):
        if i < 0 or i >= self.nSteps:
            raise Exception("invalid index for resolution")
        if self.nSteps == 1:
            w = self.maxResolution
        else:
            w = (self.maxResolution - self.minResolution) * i / float(self.nSteps - 1) + self.minResolution
        h = w / self.ratio
        return (int(w), int(h))
    
    def frameSent(self):
        now = time.time()
        self.frameTimes.append(now)
        while now - self.frameTimes[0] > 10.0:
            self.frameTimes.pop(0)
        self.FPS = len(self.frameTimes) / (now - self.frameTimes[0] + 1e-10)
