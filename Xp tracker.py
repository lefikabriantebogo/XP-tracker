class XPTracker:
    def __init__(self):
        self.total_xp = 0
        self.level = 1
        self.multiplier = 100  # XP per hour

    def add_hours(self, hours):
        xp_gained = hours * self.multiplier
        self.total_xp += xp_gained
        self.level = self.total_xp // 500 + 1
        return f"+{xp_gained} XP | Total: {self.total_xp} | Level: {self.level}"


tracker = XPTracker()
print(tracker.add_hours(3))  # Example: 3 hours = +300 XP
print(tracker.add_hours(2))  # Add 2 more hours
