
class Engine:

    def __init__(self, engine_mass_, propellant_mass_, thrust_, burn_duration_):
        self.ENGINE_MASS = engine_mass_
        self.propellant_mass = propellant_mass_
        self.thrust = thrust_
        self.burn_duration = burn_duration_
        self.mass_flow_rate = self.propellant_mass / self.burn_duration

    def get_total_mass(self, time):
        return self.ENGINE_MASS + self.remaining_propellant(time)
    
    def remaining_propellant(self, time):
        return max(0, self.propellant_mass - (self.mass_flow_rate * time))
    
    def is_burning(self, time):
        if time >= self.burn_duration:
            return False
        else:
            return True
        
    def get_current_thrust(self,time):
        if self.is_burning(time):
            return self.thrust
        else:
            return 0
        