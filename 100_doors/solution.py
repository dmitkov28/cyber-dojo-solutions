class Doors:

    def __init__(self):
        self.doors = ["closed" for i in range(100)]

    def toggle_door(self, door_idx: int):
        if door_idx < 0 or door_idx >= len(self.doors):
            return False

        if self.doors[door_idx] == "closed":
            self.doors[door_idx] = "opened"
            return

        if self.doors[door_idx] == "opened":
            self.doors[door_idx] = "closed"
            return


def solve():
    doors = Doors()
    for i in range(100):
        for j in range(i, 100, i + 1):
            doors.toggle_door(j)
    print(doors.doors)
    
    
if __name__ == "__main__":
    solve()
