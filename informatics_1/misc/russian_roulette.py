from random import shuffle


class Revolver:
    def __init__(self) -> None:
        self.reload()

    def reload(self):
        self.bullets = [True] + [False] * 5
        shuffle(self.bullets)

    def trigger(self):
        if self.bullets and self.bullets.pop():
            return "BANG!"
        return "CLICK"


r = Revolver()
for _ in range(6):
    print(r.trigger())
