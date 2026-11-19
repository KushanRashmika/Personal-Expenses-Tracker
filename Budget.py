class Budget:
    def __init__(self, category, limit):
        self.category = category
        self.limit = limit

    def is_exceeded(self, total_spent) -> bool:
        if self.limit < total_spent:
            return True
        return False

    def remaining(self, total_spent) -> float:
        return self.limit - total_spent
