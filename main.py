from C_Rocket import Rocket
from Enums import E

test_run = True

if test_run:
    # modify these values such that your rocket achieves orbit
    chassis = 10
    diameter = 20
    thrusters = 10
    r = Rocket(diameter,chassis,thrusters)

def enact_stage1():
    while r.stage1() is not False:
        r.update_rocket()
        if r.y_velocity < 0:
            print('Rocket did not escape Earth gravity.')
            return False
    print('Stage 1 completed')
    
def enact_stage2():
    while r.stage2() is not False:
        r.update_rocket()
        if r.y_position > 4*10**8:
            print('Rocket zoomed past the mooon.')
            return False
        if r.y_velocity < 0:
            print('Rocket did not escape Earth gravity.')
            return False
    print('Stage 2 completed')

def enact_stage3():
    Finished = False
    while r.stage3() is not False and not Finished:
        distance_oribit = (E.DISTANCE_TO_MOON-E.MOON_RADIUS-E.ORBIT_RADIUS)-r.y_position
        if distance_oribit < 2000:
            if abs(r.y_velocity  -E.ORBIT_VELOCITY) < 20:
                return E.ORBIT_ACHIEVED
                finished = True
        r.update_rocket()
    
    if r.y_position > E.DISTANCE_TO_MOON:
        return E.CRASHED
    
if __name__ == '__main__':
    if test_run:
        try:
            enact_stage1()
            enact_stage2()
            print(enact_stage3())
            print('simulation finished')
        except TypeError as e:
            print(e)
