"""
class Father():
    def gardening(self):
        print(" i love gardening")
class Mother():
    def cooking(self):
        print("i love cooking")
class child(Father,Mother):
    def sports(self):
        print("i love sports")
c=child()
c.gardening()
c.cooking()
c.sports()
"""
class Father():
    def skills(self):
        print("gardening", "coding")
class Mother():
    def skills(self):
        print("cooking")
class child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("sports")
c=child()
c.skills()