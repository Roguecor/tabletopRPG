class dice:
        
    def d100(self):
        # Rolls x1 100 sided die or known as a percentile die
        import random
        return random.randint(1,100)

    def d20(self):
        # Rolls x1 20 sided die
        import random
        return random.randint(1,20)

    def d12(self):
        # Rolls x1 12 sided die
        import random
        return random.randint(1,12)

    def d10(self):
        # Rolls x1 10 sided die
        import random
        return random.randint(1,10)

    def d8(self):
        # Rolls x1 8 sided die
        import random
        return random.randint(1,8)

    def d6(self):
        # Rolls x1 6 sided die
        import random
        return random.randint(1,6)

    def d4(self):
        # Rolls x1 4 sided die
        import random
        return random.randint(1,4)
