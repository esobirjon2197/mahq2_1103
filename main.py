
# 2-m
class Odam:
    joriy_yil = 2026

    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh


    @classmethod
    def tugilgan_yildan(cls, ism, yil):
        return cls(ism, cls.joriy_yil - yil)


    @classmethod
    def royxatdan(cls, royxat):
            return [cls.satrdan(s) for s in royxat]


    @classmethod
    def satrdan(cls, s):
        ism, yil = s.split(":")
        return cls.tugilgan_yildan(ism, int(yil))


o = Odam.tugilgan_yildan("Sardor", 2000)
print(o.ism, o.yosh)


for x in Odam.royxatdan(["Aziz:1995", "Laylo:2008"]):
    print(x.ism, x.yosh)


