"""
Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.
Класс Gun должен иметь три метода экземпляра:
- shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf, при третьем — pif, при четвертом — paf, и так далее
- shots_count() — метод, возвращающий актуальное количество вызовов метода shoot()
- shots_reset() — метод, сбрасывающий количество вызовов метода shoot() до нуля
"""


class Gun:
    def __init__(self):
        self.test_print = "pif"
        self.shoot_count = 0

    def set_shoot(self, shoot):
        self.test_print = shoot

    def shoot(self):
        if self.test_print == "pif":
            print("pif")
            self.set_shoot("paf")
            self.shoot_count += 1
        else:
            print("paf")
            self.set_shoot("pif")
            self.shoot_count += 1

    def shots_count(self):
        return self.shoot_count

    def shots_reset(self):
        self.shoot_count = 0


gun = Gun()

gun.shoot()
gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
