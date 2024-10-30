# don't change these
class E:
    G = 6.6743 * 10 ** -11  # m^3 kg^-1 s^-2 (Gravitational Constant)
    EARTH_RADIUS = 6.37 * 10 ** 6  # m (Earth Radius)
    EARTH_MASS = 5.97 * 10 ** 24  # kg (Earth Mass)
    MOON_MASS = 7.35 * 10 ** 22
    MOON_RADIUS = 1.7 * 10 ** 6
    
    DISTANCE_TO_MOON = 3.844 * 10 ** 8  # meters (distance from center of earth to center of the moon)
    TRIP_DISTANCE = DISTANCE_TO_MOON - MOON_RADIUS - EARTH_RADIUS

    THRUST_FROM_THRUSTER = 1 * 10 ** 5  # N (kgm/s^2)
    FUEL_BURN_RATE = .05  # kg/s
    THRUSTER_MASS = 200  # kg per thruster
    IMPACT_THRESHOLD = 5  # m/s for landing safety
    
    DRAG_COEFFICIENT = 0.2  # Cd for a streamlined rocket
    SEA_LEVEL_AIR_DENSITY = 1.225  # kg/m^3 (at sea level)
    SCALE_HEIGHT = 8400  # meters (scale height for air density decay)
    
    ATMOSPHERIC_LIMIT = 100000  # Drag effect up to 100 km altitude

    ORBIT_ACHIEVED = 'The rocket successfully achieved orbit.'
    

    CHASSIS_MASS_MULTIPLIER = .2
    ORBIT_VELOCITY = 1600
    ORBIT_RADIUS =  100_000
    