class Tier:
    def __init__(self, tier_name, *eigenschaften, **extra_infos):
        self.tier_name = tier_name
        self.eigenschaften = eigenschaften
        self.extra_infos = extra_infos

    def print_tier_details(self):
        print(f"Tier: {self.tier_name}")

        # Eigenschaften ausgeben
        if self.eigenschaften:
            print("Eigenschaften:")
            for eigenschaft in self.eigenschaften:
                print(f"- {eigenschaft}")

        # Zusätzliche Informationen ausgeben
        if self.extra_infos:
            print("Zusätzliche Infos:")
            for key, value in self.extra_infos.items():
                print(f"{key}: {value}")

# Beispielaufruf
tier_name = "Hund"
eigenschaften = ["treu", "verspielt", "wachsam"]
extra_infos = {"Alter": 5, "Farbe": "braun", "Gewicht": "20kg"}

tier = Tier(tier_name, *eigenschaften, **extra_infos)
tier.print_tier_details()