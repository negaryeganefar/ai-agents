import random


class VacuumEnvironment:
    """محیط 2×2 جاروبرقی — هر خانه می‌تواند کثیف یا تمیز باشد."""

    def __init__(self):
        # خانه‌ها: (0,0), (0,1), (1,0), (1,1)
        self.locations = [(0, 0), (0, 1), (1, 0), (1, 1)]
        self.dirty = {loc: random.choice([True, False]) for loc in self.locations}
        # حداقل یک خانه را کثیف کن تا شبیه‌سازی معنا داشته باشد
        self.dirty[random.choice(self.locations)] = True

    def is_dirty(self, location):
        return self.dirty[location]

    def clean(self, location):
        self.dirty[location] = False

    def state(self):
        """نمایش متنی محیط"""
        lines = []
        for row in range(2):
            cells = []
            for col in range(2):
                loc = (row, col)
                status = "🧹" if self.is_dirty(loc) else "✨"
                cells.append(f"{status}")
            lines.append(" | ".join(cells))
        return "\n".join(lines)

    def all_clean(self):
        return not any(self.dirty.values())


class ReflexVacuumAgent:
    """عامل بازتابی ساده (Simple Reflex Agent)

    قانون: اگر خانه کثیف است → تمیز کن
           در غیر این صورت → حرکت کن
    """

    def __init__(self, environment, start=(0, 0)):
        self.env = environment
        self.location = start
        self.moves = 0
        self.cleaned = 0

    def step(self):
        """یک گام تصمیم‌گیری"""
        if self.env.is_dirty(self.location):
            self.env.clean(self.location)
            self.cleaned += 1
            action = "CLEAN"
        else:
            action = self._choose_move()
        return action

    def _choose_move(self):
        """حرکت به خانه همسایه — اول راست، بعد پایین، بعد چپ، بعد بالا"""
        row, col = self.location
        neighbors = [(row, col + 1), (row + 1, col), (row, col - 1), (row - 1, col)]
        for n in neighbors:
            if n in self.env.locations:
                self.location = n
                self.moves += 1
                return f"MOVE to {n}"
        return "STAY"

    def run(self, max_steps=50, verbose=True):
        """اجرای عامل تا پاک شدن کامل محیط"""
        if verbose:
            print("=" * 40)
            print("  شروع شبیه‌سازی جاروبرقی 2×2")
            print("=" * 40)
            print("\nوضعیت اولیه:")
            print(self.env.state())

        for step in range(1, max_steps + 1):
            action = self.step()
            if verbose:
                print(f"\nگام {step}: مکان={self.location} → اقدام={action}")
                print(self.env.state())
            if self.env.all_clean():
                if verbose:
                    print(f"\n✅ محیط تمیز شد در گام {step}")
                return step

        if verbose:
            print("\n❌ به سقف گام‌ها رسید")
        return max_steps


if __name__ == "__main__":
    random.seed(42)
    env = VacuumEnvironment()
    agent = ReflexVacuumAgent(env, start=(0, 0))
    agent.run()

    print("\n" + "-" * 40)
    print(f"تعداد حرکات: {agent.moves}")
    print(f"تعداد خانه‌های تمیزشده: {agent.cleaned}")
