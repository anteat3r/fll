from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask

hub = PrimeHub()
hand = Motor(Port.C)
util = Motor(Port.D)
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

class BaseContext:
    def __init__(self, ss=1000,sa=1000,tr=1000,ta=1000):
        self.ss = ss
        self.sa = sa
        self.tr = tr
        self.ta = ta
    def __enter__(self):
        self.oss, self.osa, self.otr, self.ota = base.settings()
        base.settings(
            straight_speed        = self.ss,
            straight_acceleration = self.sa,
            turn_rate             = self.tr,
            turn_acceleration     = self.ta,
        )
    def __exit__(self, exc_type, exc_value, traceback):
        base.settings(
            straight_speed        = self.oss,
            straight_acceleration = self.osa,
            turn_rate             = self.otr,
            turn_acceleration     = self.ota,
        )

class NoGyro:
    def __init__(self): pass
    def __enter__(self): base.use_gyro(False)
    def __exit__(self, exc_type, exc_value, traceback): base.use_gyro(True)

async def hand_goto(ang, speed=10000, wait=True):
    hang = hand.angle()
    if hang > 50:
        hang = hang - 360
    if wait:
        await hand.run_angle(speed, - ang - hang, wait=True)
    else:
        hand.run_angle(speed, - ang - hang, wait=False)

def wait_button():
    pressed = [True]
    while any(pressed):
        pressed = hub.buttons.pressed()
    while True:
        pressed = hub.buttons.pressed()
        if Button.CENTER in pressed:
            return False
        if Button.LEFT in pressed:
            return True

async def boat():
    await hand_goto(190, wait=False)
    base.straight(260, wait=False)
    await wait(700)
    await hand_goto(290, wait=False)
    await wait(100)
    base.straight(-90, wait=False)
    await wait(600)
    with BaseContext(tr=300):
        base.turn(-40, wait=False)
        await wait(250)
    await hand_goto(0, wait=False)
    base.turn(30, wait=False)
    await wait(500)
    with BaseContext(ss=1000):
        with NoGyro():
            await base.straight(-300)

async def tower():
    await hand_goto(0)
    base.straight(-680, wait=False)
    await wait(1000)
    util.run_angle(4000, 6000, wait=False)
    await wait(6000)
    base.turn(10,then=Stop.NONE)
    with NoGyro():
        await base.straight(730)

async def volume():
    with BaseContext(sa=600):
        await hand_goto(285, wait=False)
        base.straight(250,wait=False)
        await wait(1000)
        await hand_goto(270)
        with BaseContext(ss=270):
            base.straight(53, wait=False)
        await hand_goto(180, speed=200)
    await base.straight(15)
    with BaseContext(tr=30):
        await base.turn(30,then=Stop.NONE)
    with BaseContext(tr=90):
        await hand_goto(0, wait=False)
        await base.turn(30,then=Stop.NONE)
        await base.straight(110)
    with BaseContext(tr=500):
        await base.turn(-60)
        base.straight(20,wait=False)
        cnt = 0
        await hand_goto(270)
        while hub.imu.tilt()[1] < -5 and cnt < 2:
            await hand_goto(0)
            await base.turn(5)
            cnt += 1
            await hand_goto(270)
        await base.turn(10)
    with NoGyro():
        base.straight(-550,then=Stop.COAST,wait=False)
        await wait(1200)
        await hand_goto(0)

async def dragon():
    await hand_goto(190, wait=False)
    await base.turn(-25)
    await hand_goto(200, wait=False)
    await base.straight(80)
    await hand_goto(250, wait=False)
    await base.turn(40)
    await hand_goto(0, wait=False)
    with NoGyro():
        await base.straight(-100)

async def flower():
    with BaseContext(ta=900,ss=800):
        await hand_goto(230, wait=False)
        with BaseContext(sa=600):
            await base.straight(400)
        await base.turn(-30)
        with BaseContext(ss=200):
            await base.straight(85)
            await base.turn(20)
            await hand_goto(300)
            await wait(400)
            await hand_goto(250,wait=False)
            await base.turn(-20)
            await base.straight(-95)
        await hand_goto(0, wait=False)
        await base.turn(90)
        with BaseContext(sa=600):
            base.curve(200, -110,wait=False)
        await wait(1100)
        await hand_goto(280,wait=False)
        await wait(400)
        await base.straight(-200)
        await base.turn(133)
        base.straight(330,wait=False)
        await wait(1000)

        # prekazka
        await hand_goto(0,wait=False)
        await base.straight(-30)

        # press
        base.turn(-75,wait=False)
        await wait(200)
        await hand_goto(270)
        await hand_goto(0,wait=False)
        await wait(300)
        await base.turn(75)
        base.straight(30,wait=False)
        await hand_goto(300)
        await base.turn(-20)
        await base.straight(360)
        await base.turn(80)
        with BaseContext(sa=400):
            await base.curve(490, -72)
            await hand_goto(300)
            await base.turn(90)
        with NoGyro():
            with BaseContext(sa=1000):
                base.straight(700,wait=False)
                await wait(300)
                await hand_goto(0)

async def skater():
    base.straight(250,wait=False)
    await wait(650)
    await hand_goto(280,wait=False)
    await wait(300)
    base.straight(-350,wait=False)
    await wait(1000)
    await hand_goto(0)

async def skater2():
    base.straight(180,wait=False)
    await wait(300)
    await hand_goto(280,wait=False)
    await wait(300)
    base.straight(-250,wait=False)
    await wait(900)
    await hand_goto(0)

async def camera():
    await hand_goto(235)
    await base.turn(3)
    await hand_goto(200, wait=False, speed=100)
    await base.straight(300)
    await base.straight(-300)
    await hand_goto(0)

async def lever():
    await hand_goto(290, wait=False)
    with BaseContext(ss=1000, sa=500):
        await base.curve(1465, -25)
    await base.turn(65)
    await hand_goto(210)
    base.turn(-20, wait=False)
    await wait(300)
    await hand_goto(290)
    await base.turn(-30)
    await hand_goto(0, wait=False)
    with NoGyro():
        await base.straight(-650)

async def podium():
    await hand_goto(140,wait=False)
    await base.straight(200)
    base.turn(20,wait=False)
    await hand_goto(175)
    await base.turn(-40)
    await hand_goto(0,wait=False)
    await base.turn(30)
    with NoGyro():
        await base.straight(-250)

async def artist():
    await base.straight(-310)
    base.use_gyro(False)
    await base.curve(-300, -10)
    base.use_gyro(True)
    util.run_angle(1000, 2 * 1940, wait=False)
    await wait(4000)
    with BaseContext(sa=600):
        await base.straight(480)

async def film_delivery():
    await hand_goto(260)
    await base.straight(580)
    base.straight(-90,wait=False)
    await hand_goto(0)
    await base.curve(-200, 45)
    await base.turn(55)
    await base.straight(650,then=Stop.NONE)
    await base.curve(500, -80)

async def delivery():
    await hand_goto(270)
    hub.display.icon(btn_icon)
    wait_button()
    hub.display.icon(skull_icon)
    with BaseContext(sa=800):
        await base.turn(3)
        await base.straight(420)
        await hand_goto(240)
        await base.straight(-40)
        await base.turn(20)
        await base.straight(40)
    with BaseContext(sa=300, ss=500):
        await base.curve(400, 80,then=Stop.NONE)
        await base.curve(150, -67)
        await hand_goto(270)
    await base.straight(-200)
    await base.turn(-80)
    await base.straight(300)
    await hand_goto(0)
    await base.straight(-80)
    await base.turn(160)
    with BaseContext(ss=800, sa=600):
        await base.curve(720, -88)

async def run():
    await hub.speaker.beep(frequency=500, duration=100)
    await hand_goto(0)
    watch: StopWatch = None
    for i, f in enumerate(actions[1:-1]):
        hub.display.icon(btn_icon)
        wait_button()
        if i == 0: watch = StopWatch()
        hub.display.icon(skull_icon)
        await f()
        base.stop()
        print(round(watch.time()))
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

def calib():
    while True:
        pressed = hub.buttons.pressed()
        if Button.LEFT in pressed:
            await hand_goto(0)
        if Button.RIGHT in pressed:
            await hand_goto(300)
        if Button.CENTER in pressed:
            pressed = [True]
            while any(pressed):
                pressed = hub.buttons.pressed()
                await wait(10)
            break
        
def gyrotest():
    while True:
        pressed = hub.buttons.pressed()
        print(
            hub.imu.tilt(),
        end='              \r')
        wait(100)
        if Button.CENTER in pressed:
            pressed = [True]
            while any(pressed):
                pressed = hub.buttons.pressed()
                await wait(10)
            break
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
    podium,
    lever,
    artist,
    film_delivery,
    delivery,
    calib,
    gyrotest,
]

icons = [

   [[  0,100,  0,  0,  0,],
    [  0,100,100,  0,  0,],
    [  0,100,100,100,  0,],
    [  0,100,100,  0,  0,],
    [  0,100,  0,  0,  0,],],

   [[  0,100,100,  0,  0,],
    [  0,100,100,  0,  0,],
    [  0,  0,100,  0,  0,],
    [100,100,100,100,100,],
    [  0,100,100,100,  0,],],

   [[100,  0,100,  0,100,],
    [100,  0,100,  0,100,],
    [100,100,100,100,100,],
    [  0,100,100,100,  0,],
    [  0,100,100,100,  0,],],

   [[  0,  0,  0,  0,  0,],
    [  0,  0,  0,  0,100,],
    [100,  0,  0,  0,100,],
    [100,  0,100,  0,  0,],
    [  0,  0,100,  0,  0,],],

   [[  0,  0,  0,  0,  0,],
    [  0,100,  0,100,  0,],
    [100,100,100,100,100,],
    [  0,  0,  0,  0,100,],
    [100,100,100,100,100,],],

   [[  0,100,100,100,  0,],
    [  0,100,  0,100,  0,],
    [  0,100,100,100,  0,],
    [  0,  0,100,  0,  0,],
    [  0,  0,100,100,  0,],],

   [[  0,  0,100,  0,  0,],
    [100,100,100,100,100,],
    [  0,100,100,100,  0,],
    [  0,100,100,100,  0,],
    [  0,100,  0,100,  0,],],

   [[  0,  0,100,100,  0,],
    [  0,  0,100,  0,  0,],
    [100,100,100,100,100,],
    [  0,100,100,100,  0,],
    [  0,100,  0,100,  0,],],

   [[  0,  0,  0,  0,  0,],
    [100,  0,  0,  0,100,],
    [100,100,100,100,100,],
    [100,100,100,100,100,],
    [  0,100,  0,100,  0,],],

   [[  0,  0,  0,  0,100,],
    [  0,  0,100,  0,100,],
    [  0,100,  0,100,  0,],
    [  0,100,100,100,  0,],
    [100,100,100,100,100,],],

   [[100,  0,  0,  0, 0,],
    [  0,100,  0,  0, 0,],
    [  0,  0,100,  0,  0,],
    [  0,100,100,100,  0,],
    [  0,100,100,100,  0,],],

   [[  0,  0,  0,  0,  0,],
    [100,100,100,100,100,],
    [100,100,  0,100,100,],
    [  0,  0,  0,  0,  0,],
    [  0,  0,  0,  0,  0,],],

   [[  0,  0,100,100,100,],
    [100,100,  0,  0,  0,],
    [100,100,100,100,100,],
    [100,100,100,100,100,],
    [100,100,100,100,100,],],

   [[  0,100,100,100,  0,],
    [100,  0,  0,  0,100,],
    [100,100,100,100,100,],
    [100,  0,100,  0,100,],
    [  0,100,100,100,  0,],],

   [[100,  0,  0,  0,  0,],
    [  0,100,  0,  0,  0,],
    [  0,  0,100,  0,  0,],
    [  0,  0,  0,100,  0,],
    [  0,  0,  0,  0,100,],],

   [[100,  0,  0,  0,100,],
    [  0,100,100,100,  0,],
    [  0,  0,100,  0,  0,],
    [  0,  0,100,100,  0,],
    [100,100,  0,  0,100,],],
]

btn_icon = [[  0,  0,  0,  0,  0,],
            [  0,100,100,100,  0,],
            [  0,  0,100,  0,  0,],
            [  0,  0,100,  0,  0,],
            [100,100,100,100,100,],]

skull_icon = [[100,100,100,100,100,],
             [100,  0,100,  0,100,],
             [100,  0,100,  0,100,],
             [100,100,100,100,100,],
             [  0,100,  0,100,  0,],]

async def main():
    await hand_goto(0)
    print(hub.battery.voltage())
    hub.system.set_stop_button(Button.BLUETOOTH)
    await hub.speaker.beep(frequency=500, duration=100)
    cur = 1
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
            press = [True]
            while any(press):
                press = hub.buttons.pressed()
                await wait(10)
            if cur not in [0,14]:
                hub.display.icon(btn_icon)
                wait_button()
            hub.display.icon(skull_icon)
            watch = StopWatch()
            await actions[cur]()
            print(round(watch.time()))
            base.stop()
            hand.stop()
            util.stop()
        else:
            prev = False
        hub.display.icon(icons[cur])
        await wait(10)

print('-----')
run_task(main())
