import pygame

def load_images(base_path, count, scale_width, scale_height):
    #if count = 0 automatically assume its only 1 image were loading
    if(count == 0):
        image_path = f'{base_path}.png'
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (scale_width,scale_height))
        return image
    else:
        images = []
        for i in range(1, count + 1):
            image_path = f'{base_path}{i}.png'
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (scale_width,scale_height))
            images.append(image)
        return images



def handle_collisions(enemies, lasers, enemies_to_remove, lasers_to_remove):
    score = 0
    for enemy in enemies:
        for laser in lasers:
            if enemy.die(laser):
                if enemy not in enemies_to_remove:
                    score += enemy.get_points()
                    enemies_to_remove.append(enemy)
                if laser not in lasers_to_remove:
                    lasers_to_remove.append(laser)
    return score

                    

def animation(base_path, count):
    frames = load_images(base_path, count)

    current = 0
    image = frames[0]
    rect = image.get_rect()

    current+=1

    if current == len(frames): #if images in frames completed, restart the process.
         # If the end of the frames is reached, indicate that the animation is finished
        if image == len(frames):
            finished = True
        else:
            finished = False

    image = frames[current]

    rect = image.get_rect(center = rect.center)

    return finished