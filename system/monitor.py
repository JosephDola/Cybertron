import psutil
import time

class Monitor:

    def __init__(self):
        self.last=time.time()
        self.fps=0

    def update(self):
        now=time.time()
        self.fps=1/max(now-self.last,0.0001)
        self.last=now

    def cpu(self):
        return psutil.cpu_percent(interval=None)

    def ram(self):
        return psutil.virtual_memory().percent
