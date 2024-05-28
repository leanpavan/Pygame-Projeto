#import
import pygame
import spritesheet

# animation_list = []
# animation_steps = [4, 6, 3, 4]
# action = 0
# last_update = pygame.time.get_ticks()
# animation_cooldow = 150
# frame = 0
# step_counter = 0

# for animation in animation_steps:
#     temp_img_list = []
#     for _ in range(animation):
#         temp_img_list.append(spritesheet.sprite_sheet().get_image(step_counter, 24,24, 3))
#         step_counter += 1
#     animation_list.append(temp_img_list)

class create_animation():
    def __init__(self, animation_steps, last_update, animation_cooldown):
        self.animation_list = []
        self.animation_steps = animation_steps
        self.animation_cooldown = animation_cooldown
        self.action = 0
        self.frame = 0
        self.step_counter = 0
        self.last_update = last_update
    def create_animation_list(self):
        for animation in self.animation_steps:
            temp_img_list = []
            for _ in range(animation):
                temp_img_list.append(spritesheet.sprite_sheet().get_image(self.step_counter, 24,24, 3))
                self.step_counter += 1
            self.animation_list.append(temp_img_list)
    def update_animation(self,current_time):
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = current_time
        if self.frame >= len(self.animation_list[self.action]):
            self.frame = 0
            
animation = create_animation([4, 6, 3, 4], pygame.time.get_ticks(),150)