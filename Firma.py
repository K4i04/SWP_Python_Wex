
class Firma:
    def __init__(self):




class Abteilung(Firma):
    def __init__(self,AbteilungsId, Abteilungsname):
        self.AbteilungsId = AbteilungsId
        self.Abteilungsname = Abteilungsname


class Personen(Abteilung):
    def __init__(self,AbteilungsId ,Abteilungsname ,Mid, Name, Geschlecht, Rolle):
        super().__init__(AbteilungsId,Abteilungsname)
        self.Mid = Mid
        self.Name = Name
        self.Geschlecht = Geschlecht
        self.Rolle = Rolle
        @staticmethod
        def count(zahl)
            return zahl + 1


if __name__ == '__main__':
    p1 = Personen(0,"Produktion", 0, "Anton, false, arbeiter")





