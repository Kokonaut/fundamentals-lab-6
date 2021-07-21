from engine.tower import TowerSprite
from engine.util import selector_lightning


class LightningTower(TowerSprite):

    def run_attack(self, monsters_in_range):
        self.attack_func(monsters_in_range, self, 'lightning')

    def get_selector_func(self):
        return selector_lightning

    def get_attack_cooldown(self):
        return 2

    def get_attack_radius(self):
        return 300

    def get_attack_damage(self):
        return 25
