from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask
# Oranžoví týpci: skoupi vlevo, skibi vlevo, bali vpravo

hub = PrimeHub()
hand = Motor(Port.C)
util = Motor(Port.D)
# belt = Motor(Port.C)
left = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
right = Motor(Port.E)
base = DriveBase(
    left,
    right,
    88, 112,
)
base.use_gyro(True)
base.settings(
    straight_speed        = 1000,
    straight_acceleration = 1000,
    turn_rate             = 1000,
    turn_acceleration     = 1000,
)

async def hand_goto(ang, speed=10000, wait=True):
    hang = hand.angle()
    if hang > 50:
        hang = hang - 360
    if wait:
        await hand.run_angle(speed, - ang - hang, wait=True)
    else:
        hand.run_angle(speed, - ang - hang, wait=False)

def wait_button():
    while Button.LEFT not in hub.buttons.pressed():
        pass

def wait_button2():
    while Button.RIGHT not in hub.buttons.pressed():
        pass
    
async def boat():
    await hand_goto(190, wait=False)
    base.straight(260, wait=False)
    await wait(700)
    await hand_goto(290, wait=False)
    await wait(100)
    base.straight(-90, wait=False)
    await wait(600)
    base.settings(turn_rate=300)
    base.turn(-40, wait=False)
    await wait(250)
    base.settings(turn_rate=1000)
    await hand_goto(0, wait=False)
    base.turn(40, wait=False)
    await wait(400)
    base.use_gyro(False)
    await base.straight(-300)
    base.use_gyro(True)

async def tower():
    base.settings(straight_speed=1000, straight_acceleration=1000)
    await hand_goto(0)
    base.straight(-680, wait=False)
    await wait(1000)
    util.run_angle(4000,6000,wait=False)
    await wait(6000)
    base.turn(10,then=Stop.NONE)
    await base.straight(680)

async def volume():
    base.settings(straight_acceleration=600)
    await hand_goto(285, wait=False)
    base.straight(250,wait=False)
    await wait(1000)
    # wait_button2()
    await hand_goto(270)
    base.settings(straight_speed=270)
    base.straight(48, wait=False)
    base.settings(straight_speed=1000)
    await hand_goto(150, speed=200)
    await base.straight(15)
    # wait_button()
    base.settings(turn_rate=30)
    await base.turn(30,then=Stop.NONE)
    base.settings(turn_rate=90)
    await hand_goto(0, wait=False)
    await base.turn(30,then=Stop.NONE)
    # await base.turn(-60)
    await base.straight(110)
    base.settings(turn_rate=500)
    await base.turn(-60)
    base.straight(20,wait=False)
    await hand_goto(270)
    await base.turn(15)
    # await base.turn(10,then=Stop.NONE)
    base.settings(turn_rate=1000,straight_acceleration=1000,straight_speed=1000)
    # await base.turn(15)
    base.use_gyro(False)
    base.straight(-550,then=Stop.COAST,wait=False)
    await wait(1200)
    # await base.curve(-250, 70)
    # base.settings(straight_acceleration=1000)
    await hand_goto(0)
    base.use_gyro(True)

async def dragon():
    await hand_goto(190, wait=False)
    await base.turn(-15)
    await base.straight(70)
    await hand_goto(290, wait=False)
    await base.turn(15)
    await hand_goto(0, wait=False)
    await base.straight(-100)

async def pump():
    # await hand_goto(200, wait=False)
    await base.straight(570)
    await base.turn(-45)
    # await base.straight(20)
    # for i in range(1):
    await base.straight(20)
    await base.straight(-60)
    # quit() 
    await base.turn(90)
    await base.straight(150)
    await base.turn(-90)
    await hand_goto(220)
    await base.straight(50)
    await hand_goto(0)
    await base.turn(-115)
    await base.straight(700)

async def fdlower():
    await hand_goto(300, wait=False)
    base.settings(straight_acceleration=1000)
    await base.straight(200,then=Stop.NONE)
    base.settings(straight_acceleration=600)
    await base.straight(270)
    base.settings(straight_acceleration=600)
    await base.turn(-50)
    await hand_goto(0,wait=False)
    await base.straight(100)
    await base.straight(-100)
    await base.turn(60)
    base.settings(straight_speed=800)
    await base.straight(210)
    await base.turn(-60)
    await base.straight(50)
    await right.run_angle(200,-60)
    await hand_goto(300)
    # await wait_button()
    # base.settings(straight_speed=200)
    # await base.straight(130)
    # await hand_goto(260)
    # await base.straight(30)
    # await base.straight(-30)
    # await hand_goto(0, wait=False)
    # await base.straight(-140)
    # base.settings(straight_speed=1000)
    # await hand_goto(0, wait=False)
    # await base.turn(90)
    # base.settings(straight_acceleration=400)
    # await base.curve(200, -110)
    # base.settings(straight_acceleration=1000)
    # await hand_goto(300)
    await base.straight(-100)
    base.settings(turn_acceleration=500)
    await base.turn(119)
    base.settings(turn_acceleration=800)
    await base.straight(450)
    await hand_goto(0)
    await base.straight(-30)
    await base.turn(-87)
    await hand_goto(270)
    await hand_goto(0)
    await base.turn(87)
    await base.straight(30)
    await hand_goto(300)
    await base.turn(-25)
    await base.straight(340)
    await base.turn(80)
    base.settings(straight_acceleration=300)
    await base.curve(500, -75)
    await base.straight(-100)
    await base.turn(80)
    base.settings(straight_acceleration=1000)
    await base.straight(600)
    # await base.curve(450, 100)
    # await hand_goto(0)
    # await base.turn(90)
    # await base.straight(260)
    # await base.turn(45 )
    # await hand_goto(300)
    # await base.turn(-10)
    # await base.straight(-400)
    # await base.curve(-300, -45)
    # await base.curve(300, 90)
    await hand_goto(0)

async def flower():
    base.settings(turn_acceleration=900)
    base.settings(straight_speed=800)
    await hand_goto(230, wait=False)
    base.settings(straight_acceleration=600)
    await base.straight(400)
    base.settings(straight_acceleration=1000)
    await base.turn(-30)
    base.settings(straight_speed=200)
    await base.straight(85)
    base.turn(20,wait=False)
    # wait_button()
    await hand_goto(300)
    await wait(400)
    await hand_goto(250,wait=False)
    await base.turn(-20)
    await base.straight(-95)
    # wait_button()
    # await base.straight(50)
    # await hand_goto(260)
    # await base.straight(30)
    # await base.straight(-30)
    # await hand_goto(0, wait=False)
    # await base.straight(-140)

    base.settings(straight_speed=1000)
    await hand_goto(0, wait=False)
    await base.turn(90)
    base.settings(straight_acceleration=600)
    base.curve(200, -110,wait=False)
    await wait(1100)
    base.settings(straight_acceleration=1000)
    await hand_goto(280,wait=False)
    await wait(400)
    await base.straight(-200)
    await base.turn(133)
    base.straight(330,wait=False)
    await wait(1000)
    # prekazka
    await hand_goto(0,wait=False)
    # await wait(500)
    # await wait(200)
    await base.straight(-30)
    base.turn(-82,wait=False)
    await hand_goto(270)
    await hand_goto(0,wait=False)
    await wait(200)
    await base.turn(82)
    base.straight(30,wait=False)
    await hand_goto(300)
    await base.turn(-20)
    await base.straight(350)
    await base.turn(80)
    base.settings(straight_acceleration=400)
    await base.curve(490, -72)
    await hand_goto(300)
    # await base.straight(-20)
    await base.turn(90)
    base.settings(straight_acceleration=1000)
    base.straight(650,wait=False)
    await wait(300)
    # await base.curve(450, 100)
    # await hand_goto(0)
    # await base.turn(90)
    # await base.straight(260)
    # await base.turn(45 )
    # await hand_goto(300)
    # await base.turn(-10)
    # await base.straight(-400)
    # await base.curve(-300, -45)
    # await base.curve(300, 90)
    await hand_goto(0)

async def skater():
    base.settings(straight_acceleration=1000)
    base.settings(straight_speed=1000)
    base.straight(250,wait=False)
    await wait(650)
    await hand_goto(280,wait=False)
    await wait(300)
    base.straight(-350,wait=False)
    await wait(1000)
    await hand_goto(0)

async def skater2():
    base.settings(straight_acceleration=1000)
    base.settings(straight_speed=1000)
    base.straight(180,wait=False)
    await wait(300)
    await hand_goto(280,wait=False)
    await wait(300)
    base.straight(-250,wait=False)
    await wait(900)
    await hand_goto(0)



async def camera():
    base.settings(straight_acceleration=1000,straight_speed=1000)
    await hand_goto(235)
    await base.turn(3)
    await base.straight(300)
    await base.straight(-300)
    await hand_goto(0)

async def podium():
    await hand_goto(140,wait=False)
    await base.straight(200)
    base.turn(20,wait=False)
    await hand_goto(175)
    await base.turn(-40)
    await hand_goto(0,wait=False)
    await base.turn(30)
    base.use_gyro(False)
    await base.straight(-250)
    base.use_gyro(True)


async def artist():
    base.settings(straight_speed=300, straight_acceleration=300)
    await base.straight(-370)
    left.run_angle(500, 60)
    right.run_angle(100, -100,wait=False)
    await util.run_angle(1000, 3600)
    # wait_button()
    await base.turn(-5)
    await base.straight(200, then=Stop.NONE)
    base.settings(straight_speed=1000, straight_acceleration=1000)
    await base.straight(300)
    # util.run_target(300, 0, wait=False)
    await hand_goto(0)


# 🟦 🟩 🟪 🟥 🩷
async def film_delivery():
    await hand_goto(260)
    await base.straight(580)
    # await base.turn(-15)
    # await base.straight(200)
    base.straight(-90,wait=False)
    await hand_goto(0)
    # await base.straight(80)
    await base.curve(-200, 45)
    # base.settings(turn_rate=1000,turn_acceleration=1000)
    await base.turn(55)
    # wait_button()
    base.settings(straight_acceleration=1000,straight_speed=1000,turn_acceleration=1000,turn_rate=1000)  
    await base.straight(650,then=Stop.NONE)
    await base.curve(500, -80)
    base.settings(straight_acceleration=1000)  

async def new_film_delivery():
    # await base.curve(900, 75)
    base.settings(straight_acceleration=1000,straight_speed=1000)
    base.settings(turn_rate=1000,turn_acceleration=1000)
    await base.straight(50,then=Stop.NONE)
    await base.curve(1100,-78)
    # await base.curve(2350, -42)


async def delivery():
    await hand_goto(270)
    wait_button()
    base.settings(straight_acceleration=800)
    await base.turn(3)
    await base.straight(450)
    await base.straight(-30)
    await base.turn(20)
    await hand_goto(250)
    base.settings(straight_acceleration=300)
    await base.curve(400, 80,then=Stop.NONE)
    # wait_button()
    await base.curve(150, -67)
    await base.straight(80)
    await hand_goto(270)
    base.settings(straight_acceleration=1000)
    await base.straight(-280)

    # await base.straight(-40)
    # await hand_goto(300)
    # await base.straight(-160)

    await base.turn(-80)
    await base.straight(290)
    await hand_goto(0)
    await base.straight(-80)
    await base.turn(160)
    base.settings(straight_speed=600)
    await base.curve(740, -85)
    base.settings(straight_speed=1000)
    # await base.turn(-55)
    # await base.straight(50)

    # await base.turn(-15)
    # await hand_goto(280)
    # await base.straight(50)
    # await hand_goto(230)
    # await base.turn(-37)
    # await hand_goto(280)
    # await hand_goto(0, wait=False)
    # await base.straight(150)

def between(watch):
    base.stop()
    base.reset()
    print(watch.time())
    wait_button()
 
def between2():
    base.stop()
    base.reset()
    wait_button2() 

async def run() -> None:
    await hub.speaker.beep(frequency=500, duration=100)
    await hand_goto(0)
    watch: StopWatch = None
    for i, f in enumerate(actions[1:]):
        if i == 0: watch = StopWatch()
        wait_button()
        await f()
    base.stop()
    base.reset()
    end = watch.time()
    print(end)
    fin = round(end/1000)
    if fin > 99:
        fin -= 100
    hub.display.number(fin)
    pressed = []
    while not any(pressed):
        pressed = hub.buttons.pressed()
        await wait(10)

actions = [
    run,
    boat,
    tower,
    volume,
    dragon,
    flower,
    skater,
    skater2,
    camera,
    artist,
    film_delivery,
    delivery,
]

async def main():
    hub.system.set_stop_button(Button.BLUETOOTH)
    cur = 0
    prev = False
    while True:
        pressed = hub.buttons.pressed()
        if Button.LEFT in pressed:
            if not prev:
                cur = (cur - 1) % len(actions)
                prev = True
        elif Button.RIGHT in pressed:
            if not prev:
                cur = (cur + 1) % len(actions)
                prev = True
        elif Button.CENTER in pressed:
            press = []
            while any(press):
                press = hub.buttons.pressed()
                await wait(10)
            # hub.system.set_stop_button(Button.CENTER)
            hub.display.icon([[100,100,100,100,100,],
                              [100,  0,100,  0,100,],
                              [100,  0,100,  0,100,],
                              [100,100,100,100,100,],
                              [  0,100,  0,100,  0,],])
            await actions[cur]()
            # hub.system.set_stop_button(Button.BLUETOOTH)
        else:
            prev = False
        hub.display.number(cur)
        await wait(10)

print('-----')
run_task(main())
