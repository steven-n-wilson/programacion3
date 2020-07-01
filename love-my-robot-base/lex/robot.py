import cozmo
from flask import Flask
from cozmo import util,lights, action
import requests, random,time,json
from cozmo.util import degrees, distance_mm, speed_mmps
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
from cozmo import util, lights

app = Flask(__name__)
var = []
r = {"lmr": "SOUND ALien"}

def sayText(robot: cozmo.robot.Robot):
    robot.say_text(new).wait_for_completed()

def count(robot: cozmo.robot.Robot):
    for i in range(int(new)):
        robot.say_text(str(i+1)).wait_for_completed()

def sayYes(robot: cozmo.robot.Robot):
    robot.say_text("yiis", voice_pitch = -5.0).wait_for_completed()
    cont = 1
    while cont < 3:
        robot.set_head_angle(cozmo.util.Angle(-0.3), duration = 0).wait_for_completed()
        robot.set_head_angle(cozmo.util.Angle(0.7), duration = 0).wait_for_completed()
        cont += 1

def sound(robot: cozmo.robot.Robot):
    sounds = {
    "Alien" : cozmo.audio.AudioEvents.Sfx_Alien_Invasion_Ufo,
    "Brick":cozmo.audio.AudioEvents.Sfx_Brick_Bash,
    "Orchestra": cozmo.audio.AudioEvents.SfxGameWin
}

    robot.play_audio(sounds[new])
    time.sleep(1.0)
    robot.play_audio(cozmo.audio.AudioEvents.MusicStyle80S1159BpmLoop)
    time.sleep(2.0)
    robot.play_audio(cozmo.audio.AudioEvents.MusicStyle80S1159BpmLoopStop)
    robot.play_audio(cozmo.audio.AudioEvents.MusicTinyOrchestraInit)
    time.sleep(1.0)
    robot.play_audio(cozmo.audio.AudioEvents.MusicTinyOrchestraStop)

def off_charger(robot: cozmo.robot.Robot): ##############################################################
    if robot.is_on_charger:
        robot.say_text("holaa").wait_for_completed()
        robot.drive_off_charger_contacts().wait_for_completed()
        robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()

def move(robot: cozmo.robot.Robot):
    distance = getattr(util,"distance_mm")(int(new))
    speed = getattr(util,"speed_mmps")(int(new))
    getattr(robot, "drive_straight")(distance,speed).wait_for_completed()

def turnInPlace(robot: cozmo.robot.Robot):
    turnDegrees = getattr(util,"degrees")
    getattr(robot,"turn_in_place")(turnDegrees(int(new))).wait_for_completed()

def palanquita(robot: cozmo.robot.Robot):
    if new == "Up":
        robot.move_lift(5)
    else:
        robot.move_lift(-5)
    time.sleep(1)

def turnOnLights(robot: cozmo.robot.Robot):
    colors = {
    "Red" : lights.red_light,
    "Blue": lights.blue_light,
    "Green": lights.green_light,
    "White": lights.white_light}  #lights.new

    getattr(robot,"set_all_backpack_lights")(colors[new])
    time.sleep(3)

def faceAnimation(robot: cozmo.robot.Robot):
    getattr(robot,"play_anim")(name = new).wait_for_completed()

def cubeLights(robot: cozmo.robot.Robot):
    colors = {
    "Red" : lights.red_light,
    "Blue": lights.blue_light,
    "Green": lights.green_light,
    "White": lights.white_light}
    cube1 = robot.world.get_light_cube(LightCube1Id)
    cube2 = robot.world.get_light_cube(LightCube2Id)
    cube3 = robot.world.get_light_cube(LightCube3Id)

    if cube1 is not None:
        cube1.set_lights(colors[new])
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube1Id cube - check the battery.")

    if cube2 is not None:
        cube2.set_lights(colors[new])
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube2Id cube - check the battery.")

    if cube3 is not None:
        cube3.set_lights(colors[new])
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube3Id cube - check the battery.")
    
    time.sleep(3)

def cubePickup(robot: cozmo.robot.Robot):
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=2, object_type=cozmo.objects.LightCube, timeout=30)
    lookaround.stop()
    if len(cubes) == 0:
        robot.say_text(new).wait_for_completed()
    else:
        current_action = robot.pickup_object(cubes[0], num_retries=3)
        current_action.wait_for_completed()
        if current_action.has_failed:
            robot.say_text("No thanks").wait_for_completed()

def cubeDrop(robot: cozmo.robot.Robot):
    robot.move_lift(-5)
    time.sleep(1)
    robot.drive_straight(-50,50).wait_for_completed()

def cubesRoll(robot: cozmo.robot.Robot):
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=cozmo.objects.LightCube, timeout=10)
    lookaround.stop()
    if len(cubes) == 0:
        robot.say_text(new).wait_for_completed()
    else:
        robot.run_timed_behavior(cozmo.behavior.BehaviorTypes.RollBlock, active_time=60)

def cubesStack(robot: cozmo.robot.Robot):
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=2, object_type=cozmo.objects.LightCube, timeout=30)
    lookaround.stop()
    if len(cubes) < 2:
        robot.say_text("2 cubes please").wait_for_completed()
    else:
        current_action = robot.pickup_object(cubes[0], num_retries=3)
        current_action.wait_for_completed()
        if current_action.has_failed:
            robot.say_text("No thanks").wait_for_completed()
            return
        current_action = robot.place_on_object(cubes[1], num_retries=3)
        current_action.wait_for_completed()
        if current_action.has_failed:
            robot.say_text("Sorry").wait_for_completed()
            return

        robot.say_text("Done").wait_for_completed()

def wheelie(robot: cozmo.robot.Robot):
    cube = robot.world.wait_for_observed_light_cube()
    action = robot.pop_a_wheelie(cube, num_retries=2)
    action.wait_for_completed()

def moveHead(robot: cozmo.robot.Robot):
    robot.set_head_angle(cozmo.util.Angle(int(new)), duration = 0).wait_for_completed()

actionDict = {
    "SAY": sayText, 
    "MATH": sayText, 
    "COUNT": count,
    "YES": sayYes,
    "SOUND": sound,
    "MOVE": move,
    "TURN": turnInPlace, 
    "LIFT": palanquita,
    "LIGHTS": turnOnLights,
    "ANIMATION": faceAnimation,
    "CUBE": cubeLights,
    "PICKUP": cubePickup,
    "DROP": cubeDrop,
    "ROLL": cubesRoll,
    "STACK": cubesStack,
    "HEAD": moveHead,
    "WHEELIE": wheelie,

    }

lista = r["lmr"]
var = lista.split("x")
funciones = []
new_vars = []
def call():
    for i in var:
        instruccion = i.split() #[say,hola] 
        for b in instruccion:
            found = True
            for k,v in actionDict.items():
                if b == k:
                    funciones.append(v)
                    found = False
            if found == True:
                new_vars.append(b)
    return funciones,new_vars  # funciones = [SAY, MOVE] newvars = [hola,50] ([],[])

def run(robot: cozmo.robot.Robot):               
    func = call()        
    for i in range(len(func[1])):               
        global new                               
        new = func[1][i]                    
        func[0][i](robot) #say(), move()...


@app.route('/')
def home():
    cozmo.run_program(run)
    return "hello"
   

app.run(debug=True)