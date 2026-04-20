import math
G_0 = 9.80665 # m/s^2
SEA_TEMP = 288.15 # Kelvin
GAS_CONSTANT = 287 # J/(kg * K)
EARTH_R = 6371000 # radius of earth to surface in m.
SEA_LEVEL_PRESSURE = 101325 # Pa
LAPSE_RATE = 0.0065 # K/m
T_11 = 216.65  # K, temperature at 11,000m
T_20 = 216.65  # K, temperature at 20,000m
T_32 = 228.65  # K, temperature at 32,000m
T_47 = 270.65  # K, temperature at 47,000m
T_51 = 270.65  # K, temperature at 51,000m
T_71 = 214.65  # K, temperature at 71,000m
T_84 = 186.95  # K, temperature at 84,852m
P_11 = 22632.1   # Pa, pressure at 11,000m
P_20 = 5474.89   # Pa, pressure at 20,000m
P_32 = 868.019   # Pa, pressure at 32,000m
P_47 = 110.906   # Pa, pressure at 47,000m
P_51 = 66.9389   # Pa, pressure at 51,000m
P_71 = 3.95642   # Pa, pressure at 71,000m

class Environment:

    def __init__(self, launch_altitude_, wind_speed_):
        self.launch_altitude = launch_altitude_
        self.wind_speed = wind_speed_
    
    @staticmethod
    def get_temperature(altitude):
        if altitude < 11000:
            return SEA_TEMP - (LAPSE_RATE * altitude)
        elif altitude < 20000:
            return T_20
        elif altitude < 32000:
            return T_20 + (0.001 * (altitude - 20000))
        elif altitude < 47000:
            return T_32 + (0.0028 * (altitude - 32000))
        elif altitude < 51000:
            return T_51
        elif altitude < 71000:
            return T_51 + (-0.0028 * (altitude - 51000))
        elif altitude < 84852:
            return T_71 + (-0.002 * (altitude - 71000))
        else:
            return T_84 #K constant used for temperature outside of the mesosphere
    
    @staticmethod
    def get_gravity(altitude):
        return G_0 * (EARTH_R / (EARTH_R + altitude)) ** 2
    
    @staticmethod
    def get_pressure(altitude):
        if altitude < 11000:
            return (SEA_LEVEL_PRESSURE * (SEA_TEMP / Environment.get_temperature(altitude)) ** (G_0/ (GAS_CONSTANT * LAPSE_RATE)))
        elif altitude < 20000:
            return P_11 * math.exp((-1 * G_0 * (altitude - 11000)) / (GAS_CONSTANT * T_11))
        elif altitude < 32000:
            return (P_20 * (T_20 / Environment.get_temperature(altitude)) ** (G_0/ (GAS_CONSTANT * 0.001)))
        elif altitude < 47000:
            return (P_32 * (T_32 / Environment.get_temperature(altitude)) ** (G_0/ (GAS_CONSTANT * 0.0028)))
        elif altitude < 51000:
            return P_47 * math.exp((-1 * G_0 * (altitude - 47000)) / (GAS_CONSTANT * T_47))
        elif altitude < 71000:
            return (P_51 * (T_51 / Environment.get_temperature(altitude)) ** (G_0/ (GAS_CONSTANT * -0.0028)))
        elif altitude < 84852:
            return (P_71 * (T_71 / Environment.get_temperature(altitude)) ** (G_0/ (GAS_CONSTANT * -0.002)))
        else:
            return 0.3734 # Pa, constant for air pressure over altitudes of 84852 or greater

    @staticmethod
    def get_air_density(altitude):
        return Environment.get_pressure(altitude) / (GAS_CONSTANT * Environment.get_temperature(altitude))
    
