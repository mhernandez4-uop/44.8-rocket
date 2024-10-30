from Enums import E

class Rocket:
    def __init__(self, rocket_diameter, chassis, thrusters):
        self.chassis = chassis
        self.thrusters = thrusters
        self.diameter = rocket_diameter
        self.fuel = (self.diameter * .5)**2 * 3.14 * self.chassis * 1.2
        
        self.y_velocity = 0
        self.y_position = E.EARTH_RADIUS
        self.distance_to_moon = E.DISTANCE_TO_MOON - self.y_position  # this should update as the rocket travels

    def fire_thrusters(self, direction=1, proportion=1):
        # Goal: Modify the rocket's velocity by firing thrusters. The direction and proportion of thrust
        # should be used to control the change in velocity. Fuel should be consumed proportionally based on
        # the thrust used. If fuel runs out, stop firing thrusters and provide feedback.

        pass  # Implement logic here

    def get_rocket_mass(self):
        # Goal: Calculate and return the total mass of the rocket. This mass should include:
        # 1. The mass of the thrusters.
        # 2. The mass of the chassis, based on its size and the chassis multiplier.
        # 3. The current mass of the remaining fuel.

        pass  # Implement logic here

    def get_air_density(self):
        # Goal: Determine the air density at the rocket’s current altitude. If the rocket is within the atmosphere,
        # calculate the air density. If it is above the atmosphere, return 0 to indicate no air density.
        
        pass  # Implement logic here

    def get_drag(self):
        # Goal: Calculate the drag force acting on the rocket due to its velocity and the air density at its altitude.
        # The drag should depend on the rocket's velocity, its cross-sectional area, and the air density.
        # If the rocket is above the atmosphere, there should be no drag.

        pass  # Implement logic here

    def get_acceleration_due_to_gravity(self, other_object=E.EARTH_MASS):
        # Goal: Compute the gravitational acceleration acting on the rocket due to the specified object.
        # This can either be Earth or the Moon. The gravitational acceleration should depend on the mass
        # of the object and the distance from the rocket to the object's center.

        pass  # Implement logic here

    def update_rocket(self):
        # Goal: Update the rocket’s state. Apply the gravitational forces from Earth and the Moon,
        # factor in the effects of drag, and then update the rocket’s position and velocity.
        # Finally, check if the rocket has landed or crashed on Earth, and return the appropriate result.

        pass  # Implement logic here

    def display_rocket_progress(self):
        # Goal: Output the current status of the rocket. This includes the rocket’s altitude, velocity,
        # fuel remaining, and any other relevant data for debugging purposes.
        
        pass  # Implement logic here

    # look at main to see how the stages are handled
    def stage1(self):
        # this is liftoff.
        # return True when you wish to move to the next stage.

    def stage2(self):
        # this is travel (the rocket is not firing any thrusters)
        # return True when wish to move to the next stage

    def stage3(self):
        # this is landing it will be called until the rocket crashes
        # returns to earth or lands