import pyautogui as pg
from pynput.keyboard import Key, Listener
from time import sleep

# Add a set distance option for user (he needs to specify his rod (no pun intended))

def throw_fish(key):
    if key == key.f1:
        pg.mouseDown(button='left')
        sleep(0.956) # figure how long
        pg.mouseUp(button='left')

def main():
    with Listener(on_press=lambda key: throw_fish(key),) as listener:
        listener.join()

if __name__ == "__main__":
    main()
