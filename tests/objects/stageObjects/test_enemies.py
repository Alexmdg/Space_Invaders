# import os, sys, inspect
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# parentdir2 = os.path.dirname(parentdir)
# parentdir3 = os.path.dirname(parentdir2)
# sys.path.append(parentdir3)
# from objects.stageObjects.enemies import EnemyArmy, SpaceOcto

class Test_EnemyArmy:
    army = EnemyArmy(SpaceOcto, 5, 5, 50, '1')

    def test_init_(self):
        errors = []
        if len(self.army.sprites()) != 25:
            errors.append(f'army length:{self.army.sprites()}')
        if type(self.army.sprites()) is not SpaceOcto:
            errors.append(f'army type: {type(self.army.sprites())}')
        if self.army.enemy_type is not SpaceOcto:
            errors.append(f'enemy type : {self.army.enemy_type}')
        assert len(errors) == 0

