__author__ = 'Syne Ardwin'

from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.effects import Print,Stars,Wipe
from asciimatics.renderers import FigletText

def screen_welcome(screen):
    effects = [
        Print(
            screen,
            FigletText("Hc Svnt Dracones", font='stop'),
            (screen.height//2-6)
        ),
        Print(
            screen,
            FigletText("Character Creator", font='stop'),
            (screen.height//2)
        ),
        Print(
            screen,
            FigletText("Press SPACE", font='small'),
            (screen.height//2+12)
        ),
        Stars(screen, 64)
    ]
    #screen.print_at(str(screen.height),0,0)
    #screen.refresh()
    screen.play([Scene(effects, 500)])

Screen.wrapper(screen_welcome)