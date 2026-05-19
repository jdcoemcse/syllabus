import pygame,numpy as np
from scipy.special import comb
pygame.init()
WIDTH,HEIGHT,FPS=800,500,60
COLORS={"sun_day":(255,204,0),"sun_set":(255,140,0),"moon":(220,220,255),
        "sky_day":(135,206,250),"sky_night":(10,10,50),
        "ground_day":(34,139,34),"ground_night":(10,30,10)}
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Day & Night Transition")
def bezier_curve(points,num):
    points=np.array(points)
    n,t=len(points)-1,np.linspace(0,1,num)
    return sum(np.outer(comb(n,i)*(t**i)*((1-t)**(n-i)),p)for i,p in enumerate(points))
num_frames=WIDTH//2
sun_path=bezier_curve([[-50,HEIGHT-50],[WIDTH//2,100],[WIDTH+50,HEIGHT-50]],num_frames)
moon_path=bezier_curve([[-50,HEIGHT-50],[WIDTH//2,120],[WIDTH+50,HEIGHT-50]],num_frames)
def draw_crescent_moon(x,y,radius,sky_color):
    pygame.draw.circle(screen,COLORS["moon"],(int(x),int(y)),radius)
    pygame.draw.circle(screen,sky_color,(int(x+radius//3),int(y)),radius)
clock,frame,sun_active=pygame.time.Clock(),0,True
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    transition=frame/num_frames if sun_active else 1-(frame/num_frames)
    sky=[(1-transition)*d+transition*n for d,n in zip(COLORS["sky_day"],COLORS["sky_night"])]
    ground=[(1-transition)*d+transition*n for d,n in zip(COLORS["ground_day"],COLORS["ground_night"])]
    screen.fill(tuple(map(int,sky)))
    pygame.draw.rect(screen,tuple(map(int,ground)),(0,HEIGHT-50,WIDTH,50))
    x,y=(sun_path if sun_active else moon_path)[frame]
    if sun_active:
        sun_color=[(1-transition)*d+transition*n for d,n in zip(COLORS["sun_day"],COLORS["sun_set"])]
        pygame.draw.circle(screen,tuple(map(int,sun_color)),(int(x),int(y)),30)
    else:
        draw_crescent_moon(x,y,30,tuple(map(int,sky)))
    pygame.display.flip()
    clock.tick(FPS)
    frame=(frame+1)%num_frames
    if frame==0:
        sun_active=not sun_active