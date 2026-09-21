class MagicToyCatalog:
    def __init__(self):
        self.toys = {}
        self._secret_offer = "Free plushie with any purchase!"

    def __setitem__(self, name, details):
        self.toys[name] = details

    def __getitem__(self, name):
        return self.toys.get(name, ("Unknown", "Not in stock"))

    def __delitem__(self, name):
        if name in self.toys:
            del self.toys[name]
            print(f"Poof! {name} vanished from the catalog!")
        else:
            raise MagicToyError(f"✨ {name} doesn't exist in our dimension")

    def __contains__(self, name):
        return name in self.toys

    def __len__(self):
        return len(self.toys)

    def __iter__(self):
        return iter(self.toys.items())

    def __add__(self, other):
        combined = MagicToyCatalog()
        combined.toys = {**self.toys, **other.toys}
        return combined

    def __str__(self):
        header = "🔮 Magic Toy Catalog 🔮\n"
        items = "\n".join([f"- {name}: ${price} ({desc})"
                          for name, (price, desc) in self.toys.items()])
        return header + (items if items else "✨ Empty (for now)")

    def __repr__(self):
        return f"<MagicToyCatalog: {len(self)} toys>"

    def __call__(self, discount=0):
        return "\n".join([f"{name}: ${price * (1 - discount/100):.2f}"
                         for name, (price, desc) in self.toys.items()])

class MagicToyError(Exception):
    pass

kids_toys = MagicToyCatalog()
collector_editions = MagicToyCatalog()

kids_toys["RoboDog"] = (49.99, "Self-charging robot dog")
kids_toys["MagicKit"] = (29.95, "150 magic tricks set")
collector_editions["DragonStatue"] = (199.99, "Limited edition crystal dragon")

mega_catalog = kids_toys + collector_editions

print(mega_catalog["RoboDog"])

print("DragonStatue" in mega_catalog)

print(f"Total toys: {len(mega_catalog)}")

for name, details in mega_catalog:
    print(f"{name}: {details[1]}")

print(mega_catalog)

print("\n🔥 FLASH SALE 🔥")
print(mega_catalog(20))

del mega_catalog["MagicKit"]
