import sys

# رفع مشکل نمایش حروف فارسی در ترمینال ویندوز
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

TARGET_TEMP = 20       # دمای هدف
STEP = 0.5             # تغییر دما در هر گام (درجه)


class Room:
    """یک خانه از محیط با دمای مشخص"""

    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    def heat(self):
        """روشن شدن گرمکن → دما بالا می‌رود"""
        self.temperature += STEP

    def cool(self):
        """روشن شدن سرمایش → دما پایین می‌رود"""
        self.temperature -= STEP

    def status(self):
        if self.temperature < TARGET_TEMP:
            return "گرمکن ON"
        elif self.temperature > TARGET_TEMP:
            return "سرمایش ON"
        return "خاموش"


class SimpleReflexThermostatAgent:
    """عامل واکنشی ساده کنترل دما (Simple Reflex Agent)

    قانون بازتابی برای هر خانه:
        اگر دما < 20 → گرمکن را روشن کن
        اگر دما > 20 → سرمایش را روشن کن
        اگر دما == 20 → هیچکاری نکن

    عامل هیچ حافظه‌ای ندارد و فقط بر اساس
    ادراک لحظه‌ای (دمای فعلی) تصمیم می‌گیرد.
    """

    def __init__(self, rooms):
        self.rooms = rooms

    def perceive_and_act(self):
        """یک چرخه کامل: ادراک → تصمیم → اقدام"""
        actions = []
        for room in self.rooms:
            if room.temperature < TARGET_TEMP:
                room.heat()
                actions.append(f"{room.name}: گرمکن روشن شد → {room.temperature}°C")
            elif room.temperature > TARGET_TEMP:
                room.cool()
                actions.append(f"{room.name}: سرمایش روشن شد → {room.temperature}°C")
            else:
                actions.append(f"{room.name}: در دمای هدف ✅ ({room.temperature}°C)")
        return actions

    def run(self, max_steps=20):
        """اجرای شبیه‌سازی تا رسیدن هر دو خانه به دمای هدف"""
        print("=" * 55)
        print("   عامل واکنشی ساده کنترل دما | هدف: 20 درجه")
        print("=" * 55)
        self._print_state("وضعیت اولیه")

        for step in range(1, max_steps + 1):
            print(f"\n--- گام {step} ---")
            for action in self.perceive_and_act():
                print(f"  {action}")
            self._print_state()

            if all(abs(r.temperature - TARGET_TEMP) < 1e-9 for r in self.rooms):
                print(f"\n✅ هر دو خانه به دمای هدف رسیدند در گام {step}")
                return step

        print("\n❌ به سقف گام‌ها رسید")
        return max_steps

    def _print_state(self, label="وضعیت فعلی"):
        temps = "  |  ".join(f"{r.name}: {r.temperature}°C" for r in self.rooms)
        print(f"[{label}] {temps}")


if __name__ == "__main__":
    rooms = [
        Room("خانه ۱", 17),
        Room("خانه ۲", 24),
    ]
    agent = SimpleReflexThermostatAgent(rooms)
    agent.run()
