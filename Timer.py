import pygame.time

class Timer:
    def __init__(self, duration, callback, autostart = False, repeat = True):
        self.duration = duration
        self.repeat = repeat
        self.autostart = autostart
        self.callback = callback
        
        self.running = False
        self.start = 0
        if autostart:
            self.startTimer()
    def update(self):
        if self.running:
            if pygame.time.get_ticks() - self.start >= self.duration:
                if self.callback:
                    self.callback()
                    self.stopTimer()
                    if (self.repeat):
                        self.startTimer()

    def startTimer(self):
        self.start = pygame.time.get_ticks()
        self.running = True
    def stopTimer(self):
        self.running = False
        self.start = 0