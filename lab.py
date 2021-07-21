
monster_1_folder = 'assets/enemy_1/'
monster_2_folder = 'assets/enemy_2/'
monster_3_folder = 'assets/enemy_3/'
monster_4_folder = 'assets/enemy_4/'


class FastMonster:

    def __init__(self, x, y, spawn_delay):
        self.x = x
        self.y = y
        self.spawn_delay = spawn_delay
        self.assets = monster_2_folder
        self.path = self.build_path()

        self.hp = 35
        self.speed = 90

        self.defeated = False

    def take_damage(self, damage):
        self.monster_2_folder = monster_2_folder
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.defeated = True

    def build_path(self):
        # Only goes right
        i = self.x
        path = []
        while i < 1.0:
            i += 1
            path.append((i, self.y,))
        return path
