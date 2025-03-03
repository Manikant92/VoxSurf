import llms.deepgram
import pygame
import os

chosen_model = "deepgram"


def play_sound(data):
    try:
        if chosen_model == "deepgram":
            llms.deepgram.make_audio(data)
            pygame.mixer.init()
            sound = pygame.mixer.Sound("audio.mp3") # os.path.dirname(__file__) + 
            sound.play()
    except:
        print('Exception')
