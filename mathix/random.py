class random:
    def __init__(self, seed=None):
        if seed is None:
            seed = id(object()) % 2 ** 31  # Genera una semilla semialeatoria
        self.seed = seed
        self.modulus = 2 ** 31
        self.a = 1103515245
        self.c = 12345

    def random(self):
        self.seed = (self.a * self.seed + self.c) % self.modulus
        return self.seed / self.modulus

    def randint(self, a, b):
        return a + int(self.random() * (b - a + 1))

    def uniform(self, a, b):
        return a + self.random() * (b - a)

    def choice(self, seq):
        if not seq:
            raise ValueError("La secuencia está vacía")
        return seq[int(self.random() * len(seq))]

    def shuffle(self, seq):
        for i in reversed(range(1, len(seq))):
            j = int(self.random() * (i + 1))
            seq[i], seq[j] = seq[j], seq[i]
        return seq

    def sample(self, seq, k):
        if k > len(seq):
            raise ValueError("La muestra es mayor que la secuencia")
        copied = seq[:]
        self.shuffle(copied)
        return copied[:k]

    def choices(self, population, k=1, weights=None):
        if weights:
            total = sum(weights)
            cum_weights = []
            cumsum = 0
            for w in weights:
                cumsum += w
                cum_weights.append(cumsum)
            return [population[self._bisect(cum_weights, self.random() * total)] for _ in range(k)]
        else:
            return [self.choice(population) for _ in range(k)]

    def _bisect(self, cum_weights, x):
        lo, hi = 0, len(cum_weights)
        while lo < hi:
            mid = (lo + hi) // 2
            if x < cum_weights[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo
