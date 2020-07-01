import requests,json,cozmo,time
from cozmo import util,lights

# # url = "http://localhost:8080/"
# # r = requests.get(url).json()

r = {"lmr": "SAY hello \n MOVE 50 \n MOVE 50"}
lista = r["lmr"]
var = lista.split(" \n ")
def creator(parametro):
    for mini in var:
        instruccion = mini.split()
        for each in range(len(instruccion)):
            if instruccion[each] == parametro:
                new_var = instruccion[each+1]
                return new_var

def sayText(robot: cozmo.robot.Robot):
    robot.say_text(new).wait_for_completed()

def move(robot: cozmo.robot.Robot):
    distance = getattr(util,"distance_mm")(new)
    speed = getattr(util,"speed_mmps")(new)
    getattr(robot, "drive_straight")(distance,speed).wait_for_completed()

def turnInPlace(robot: cozmo.robot.Robot):
    turnDegrees = getattr(util,"degrees")
    getattr(robot,"turn_in_place")(turnDegrees(new)).wait_for_completed()

# def turnOnLights(robot: cozmo.robot.Robot):
#     light = getattr(lights,new)
#     getattr(robot,"set_all_backpack_lights")(light)
#     time.sleep(3)

actionDict = {
    "SAY": sayText, 
    "MOVE": move, 
    "TURN": turnInPlace, 
    # "LIGHTS": turnOnLights,
    }

def call():
    for i in var:
        instruccion = i.split()
        for b in instruccion:
            for k,v in actionDict.items():
                if b == k:
                    global new
                    new = creator(k)
                    cozmo.run_program(v)
# cont = 0 
# while cont < len(var):
call()
# cont += 1

