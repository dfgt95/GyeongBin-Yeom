from pico2d import *
from helper import *

open_canvas()
img = load_image('../../res/run_animation.png')
grass = load_image('../../res/grass.png')

running = True
frame = 0

pos = get_canvas_width() // 2, 80
done = True

while running:
    clear_canvas()
    grass.draw(400,30)
    

    if not done:
        pos, done = move_toward(pos=pos, delta=delta_1, target=target)
    img.clip_draw(frame * 100, 0 ,100, 100, pos[0] ,pos[1])
    update_canvas()
    frame = (frame +1) % 8
    evts = get_events()
    delay(0.05)
    for event in evts:
        global x ,y
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            target = (event.x,get_canvas_height() - 1 - event.y)
            delta_1 = delta(pos=(pos[0],pos[1]), target=target, speed=30)
            pos, done = move_toward(pos=pos, delta=delta_1, target=target)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False