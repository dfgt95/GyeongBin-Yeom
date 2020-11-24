from pico2d import *
import gfw
import stick
import bg
import title_state

def enter():
    gfw.world.init(['bg', 'stick', 'Trigon', 'ui'])

    bg.init()
    gfw.world.add(gfw.layer.bg, bg)

    stick.init()
    gfw.world.add(gfw.layer.stick, stick)

    global font
    font = gfw.font.load('res/ConsolaMalgun.ttf', 20)
    
    global score
    score = 0

def update():
    global score

def draw():
    gfw.world.draw()
    score_pos = 20, get_canvas_height() - 30
    font.draw(*score_pos, 'Score: %.1f' % score, (255,255,255))

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.change(title_state)

def exit():
    pass

def pause():
    pass
def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()