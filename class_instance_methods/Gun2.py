"""
Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.
Класс Gun должен иметь один метод экземпляра:
shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf, при третьем — pif, при четвертом — paf, и так далее
"""


class Gun:
    def __init__(self):
        self.test_print = "pif"

    def set_shoot(self, shoot):
        self.test_print = shoot

    def shoot(self):
        if self.test_print == "pif" :
            print("pif")
            self.set_shoot("paf")
        else:
            print("paf")
            self.set_shoot("pif")




gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()
