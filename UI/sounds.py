import pygame
import threading

class SoundManager:
    def __init__(self):
        self.enabled = True
        pygame.mixer.init()

    def play(self, filepath):
        if self.enabled:
            threading.Thread(target=self._play_sound, args=(filepath,), daemon=True).start()

    def _play_sound(self, filepath):
        sound = pygame.mixer.Sound(filepath)
        sound.play()

    def toggle(self):
        self.enabled = not self.enabled
