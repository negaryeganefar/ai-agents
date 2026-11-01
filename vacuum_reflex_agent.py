import sys
import random

# رفع مشکل نمایش حروف فارسی در ترمینال ویندوز
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

# مسیر ثابت حرکت (نوار نقاله‌ای) — همه خانه‌ها را پوشش می‌دهد
ROUTE = [(0, 0), (0, 1), (1, 1), (1, 0)]


class VacuumEnvironment:
    """محیط ۲×۲ جاروبرقی — هر خانه کثیف یا تمیز است."""

    def __init__(self):
        # ساخت خانه‌های محیط، هر کدام با وضعیت تصادفی
        self.dirty = {(r, c): random.choice([True, False])
                      for (r, c) in ROUTE}
        # تضمین اینکه حداقل یک خانه کثیف باشد
        self.dirty[random.choice(ROUTE)] = True

    def is_dirty(self, location):
        """ادراک: آیا این خانه کثیف است؟"""
        return self.dirty[location]

    def clean(self, location):
        """اقدام: تمیز کردن خانه"""
        self.dirty[location] = False

    def all_clean(self):
        """آیا همه خانه‌ها تمیز هستند؟"""
        return not any(self.dirty.values())

    def render(self):
        """نمایش گرافیکی متنی محیط"""
        lines = []
        for r in range(2):
            cells = []
            for c in range(2):
                cells.append("🧹" if self.dirty[(r, c)] else "✨")
            lines.append("   ".join(cells))
        return "\n".join(lines)


class SimpleReflexVacuumAgent:
    """عامل واکنشی ساده جاروبرقی

    قوانین بازتابی:
        IF کثیف   → CLEAN
        IF تمیز   → MOVE (طبق مسیر ثابت)
    """

    def __init__(self, environment):
        self.env = environment
        self.location = ROUTE[0]     # شروع از خانه (0,0)
        self.route_index = 0         # اندیس مسیر ثابت
        self.cleaned_count = 0       # شمارنده تمیزکاری‌ها
        self.move_count = 0          # شمارنده حرکات

    # ---------- مرحله ۱: ادراک ----------
    def perceive(self):
        return self.env.is_dirty(self.location)

    # ---------- مرحله ۲: تطبیق قوانین ----------
    def match_rules(self, is_dirty):
        if is_dirty:
            return "CLEAN"      # قانون ۱
        return "MOVE"           # قانون ۲

    # ---------- مرحله ۳: اقدام ----------
    def act(self, action):
        if action == "CLEAN":
            self.env.clean(self.location)
            self.cleaned_count += 1
        elif action == "MOVE":
            # حرکت به خانه بعدی مسیر ثابت (حلقه‌ای)
            self.route_index = (self.route_index + 1) % len(ROUTE)
            self.location = ROUTE[self.route_index]
            self.move_count += 1

    # ---------- اجرای حلقه اصلی ----------
    def run(self, max_cycles=10):
        print("=" * 46)
        print("  عامل واکنشی ساده — جاروبرقی ۲×۲")
        print("=" * 46)
        print("\nوضعیت اولیه محیط:")
        print(self.env.render())

        for step in range(1, max_cycles + 1):
            print(f"\n───────── گام {step} ─────────")
            print(f"موقعیت عامل: {self.location}")

            # چرخه کامل: ادراک → تطبیق → اقدام
            perception = self.perceive()                 # ادراک
            action = self.match_rules(perception)        # تطبیق قانون
            print(f"ادراک: {'کثیف 🧹' if perception else 'تمیز ✨'}"
                  f"  →  اقدام: {action}")
            self.act(action)                             # اقدام

            print("وضعیت محیط:")
            print(self.env.render())

            # قانون ۳: بررسی پایان کار
            if self.env.all_clean():
                print("\n✅ همه خانه‌ها تمیز شدند — پایان کار عامل")
                break
        else:
            print("\n❌ به سقف گام‌ها رسید")

        print(f"\nآمار: تمیزکاری={self.cleaned_count} | "
              f"حرکت={self.move_count}")


if __name__ == "__main__":
    random.seed(42)                      # برای خروجی قابل تکرار
    env = VacuumEnvironment()
    agent = SimpleReflexVacuumAgent(env)
    agent.run()
