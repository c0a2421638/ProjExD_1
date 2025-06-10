import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 =pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("fig/3.png")  # こうかとん画像のSurface
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect() #こうかとんのrect画像
    kk_rct.center = 300,200
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        time = 0
        high = 0
        key_lst = pg.key.get_pressed()
        time-=1 
        if key_lst[pg.K_UP]:  
            high-=1
        if key_lst[pg.K_DOWN]:
            high+=1
        if key_lst[pg.K_LEFT]:
            time-=1
        if key_lst[pg.K_RIGHT]:
            time+=2
        kk_rct.move_ip(time, high)
        tmr %= 3200
        screen.blit(bg_img, [-tmr, 0])
        screen.blit(bg_img2, [1600-tmr, 0])
        screen.blit(bg_img, [3200-tmr, 0])
        screen.blit(kk_img,kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()