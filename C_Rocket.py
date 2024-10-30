from Enums import E
class Rocket:
    def __init__(self, rocket_diameter, chassis, thrusters):
        self.chassis = chassis
        self.thrusters = thrusters
        self.diameter = rocket_diameter
        self.fuel = (self.diameter * .5)**2 * 3.14 * self.chassis *1.2

        self.y_velocity = 0
        self.y_position = E.EARTH_RADIUS

    def get_rocket_mass(self):
        # Step 1: Calculate the mass of the thrusters.
        # Multiply the number of thrusters (self.thrusters) by the mass of each thruster (E.THRUSTER_MASS).
        thruster_mass = None  # <-- Fill this in

        # Step 2: Calculate the chassis mass.
        # Multiply the chassis mass (self.chassis) by the diameter (self.diameter), by pi (math.pi),
        # and by the chassis mass multiplier (E.CHASSIS_MASS_MULTIPLIER).
        chassis_mass = None  # <-- Fill this in

        # Step 3: Add the fuel mass (self.fuel).
        fuel_mass = None  # <-- Fill this in

        # Step 4: Calculate the total mass by adding thruster mass, chassis mass, and fuel mass.
        total_mass = None  # <-- Fill this in

        # Return the total mass of the rocket.
        return total_mass

    def fire_thrusters(self, direction=1, proportion=1):
        # NOTE: 1 = AWAY FROM EARTH -1 = TOWARDS EARTH
        # Step 1: Check if there is enough fuel.
        # If self.fuel is greater than 0, the rocket can continue firing.
        if None:  # <-- Fill in the condition for fuel check
            # Step 2: Subtract the fuel burned during this step.
            # Multiply E.FUEL_BURN_RATE by self.thrusters and by the proportion of thrust used.
            self.fuel -= None  # <-- Fill this in
            
            # Step 3: Calculate the change in velocity.
            # Use the formula: thrust / mass * direction * proportion.
            # E.THRUST_FROM_THRUSTER gives the thrust, and self.get_rocket_mass() gives the mass.
            self.y_velocity += None  # <-- Fill this in
        else:
            # Step 4: If there's no fuel, print an out of fuel message and return.
            print('Out of fuel, distance from moon', self.distance_to_moon)
            return

  

    def get_air_density(self):
        # Step 1: Calculate the altitude of the rocket.
        # Subtract Earth's radius (E.EARTH_RADIUS) from the rocket's current position (self.y_position).
        altitude = None  # <-- Fill this in

        # Step 2: Check if the altitude is above the atmospheric limit (E.ATMOSPHERIC_LIMIT).
        # If it is, return 0 because there's no air at that altitude.
        if None:  # <-- Fill in the condition for checking atmospheric limit
            return 0

        # Step 3: If the rocket is within the atmosphere, calculate the air density using the exponential decay formula.
        #       !!!!!!!!!!!!!!!!!!!!! GOOGLE ME!!!!!!!!!!!!!!!!!!!!!!
        # Use E.SEA_LEVEL_AIR_DENSITY and E.SCALE_HEIGHT in the calculation.
        air_density = None  # <-- Fill this in

        # Return the calculated air density.
        return air_density

    def get_drag(self):
        # Step 1: Get the current air density by calling self.get_air_density().
        air_density = None  # <-- Fill this in

        # Step 2: If air_density is 0, return 0 because there's no drag without air.
        if None:  # <-- Fill in the condition for checking if air density is 0
            return 0
        
        # Step 3: Calculate the cross-sectional area of the rocket.
        # Use the formula for the area of a circle: pi * radius^2 (where radius = self.diameter / 2).
        area = None  # <-- Fill this in

        # Step 4: Calculate the drag force using the drag equation.
        # Use E.DRAG_COEFFICIENT, air_density, area, and self.y_velocity^2 in the formula.
        #   GOOGLE ME!!!!
        drag_force = None  # <-- Fill this in

        # Step 5: Divide the drag force by the rocket's mass to get the drag acceleration, and return it.
        return None  # <-- Fill this in

        
    def get_acceleration_due_to_gravity(self, other_object=E.EARTH_MASS):
        # Step 1: Check if the other object is Earth or the Moon.
        # If it's Earth, use the Earth's mass (E.EARTH_MASS) and the distance from Earth's center (self.y_position).
        if other_object == E.EARTH_MASS:
            # Step 2: Calculate the acceleration due to Earth's gravity.
            # Use the formula: a = G * M / r^2, where G is the gravitational constant and M is Earth's mass.
            # G is enumerated
            a = None  # <-- Fill this in
        else:
            # Step 3: If the other object is the Moon, calculate the distance from the rocket to the Moon.
            # Use E.DISTANCE_TO_MOON and self.y_position.
            current_distance_to_moon = None  # <-- Fill this in

            # Step 4: Calculate the acceleration due to the Moon's gravity.
            # Use the same formula: a = G * M / r^2, where M is the Moon's mass.
            a = None  # <-- Fill this in

        # Return the calculated gravitational acceleration.
        return a

    def update_rocket(self):
        # Step 1: Update the rocket's velocity by applying Earth's gravity.
        # Call self.get_acceleration_due_to_gravity() to get Earth's gravity and add it to self.y_velocity.
        self.y_velocity += None  # <-- Fill this in
        
        # Step 2: Update the rocket's velocity by applying the Moon's gravity.
        # Call self.get_acceleration_due_to_gravity(E.MOON_MASS) to get the Moon's gravity and add it to self.y_velocity.
        self.y_velocity += None  # <-- Fill this in
        
        # Step 3: Subtract the drag force from the rocket's velocity.
        # Call self.get_drag() to get the drag acceleration and subtract it from self.y_velocity.
        self.y_velocity -= None  # <-- Fill this in

        # Step 4: Update the rocket's position by adding the current velocity to self.y_position.
        self.y_position += None  # <-- Fill this in

    def display_rocket_progress(self):
        # this is used for your own debugging. I will not call it.
        pass

    # look at main to see how the stages are handled
    def stage1(self):
        # this is liftoff.
        # return False when you wish to move to the next stage.
        pass
    def stage2(self):
        # this is travel (the rocket is not firing any thrusters)
        # return False when you wish to move to the next stage
        pass
    def stage3(self):
        # this stage adjusts velocity to match orbit velocity
        # success means the velocity of the rocket is very close to E.ORBIT_VELOCITY at distance E.ORBIT_RADIUS
        # main checks to see if conditions are met this does not need to return anything.
        pass