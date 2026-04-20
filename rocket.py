import engine

class Rocket:

    def __init__(self, rocket_dry_mass_, engine_, dc_, csa_):
        self.dry_mass = rocket_dry_mass_
        self.ENGINE = engine_
        self.drag_coefficient = dc_
        self.cross_sectional_area = csa_

    def get_Rocket_Mass(self):
        return self.dry_mass + engine.get_total_mass()
