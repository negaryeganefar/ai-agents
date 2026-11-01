import sys
import random

# رفع مشکل نمایش حروف فارسی در ترمینال ویندوز
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

# ۱۰ جرم مفروض (داده ورودی)
WEIGHTS = [35, 12, 48, 7, 26, 19, 53, 41, 2, 30]


class LinearEnvironment:
    """محیط خطی مرتب‌سازی — نواری از خانه‌ها با وزن‌ها"""

    def __init__(self, weights):
        # کپی از لیست ورودی تا داده اصلی تغییر نکند
        self.items = list(weights)
        self.n = len(self.items)

    def get(self, i):
        """ادراک: وزن خانه i"""
        return self.items[i]

    def swap(self, i, j):
        """اقدام: تبادل دو خانه"""
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def is_sorted(self):
        """آیا کل خط مرتب شده؟ (فقط برای بررسی پایان)"""
        return all(self.items[i] <= self.items[i + 1]
                   for i in range(self.n - 1))

    def render(self):
        """نمایش متنی خط"""
        return " | ".join(f"{w:2d}" for w in self.items)


class SimpleReflexSorterAgent:
    """عامل واکنشی ساده مرتب‌سازی وزن‌ها (از کوچک به بزرگ)

    قوانین بازتابی:
        IF  وزن[i] > وزن[i+1] → SWAP (جای عوض کن)
        IF  وزن[i] ≤ وزن[i+1] → MOVE (یکی جلو برو)
        IF  انتهای خط         → RETURN (چرخه جدید)
        IF  چرخه بدون تبادل   → STOP  (تمام)
    """

    def __init__(self, environment):
        self.env = environment
        self.position = 0        # موقعیت فعلی عامل
        self.swap_count = 0      # شمارنده تبادل‌ها
        self.move_count = 0      # شمارنده حرکات
        self.pass_count = 0      # شمارنده چرخه‌ها

    # ---------- مرحله ۱: ادراک ----------
    def perceive(self):
        """وزن خانه فعلی و خانه مجاور را بخوان"""
        current = self.env.get(self.position)
        neighbor = self.env.get(self.position + 1)
        return current, neighbor

    # ---------- مرحله ۲: تطبیق قوانین ----------
    def match_rules(self, current, neighbor):
        if current > neighbor:
            return "SWAP"    # قانون ۱
        return "MOVE"        # قانون ۲

    # ---------- مرحله ۳: اقدام ----------
    def act(self, action):
        if action == "SWAP":
            self.env.swap(self.position, self.position + 1)
            self.swap_count += 1
        # حرکت همیشه انجام می‌شود (چه بعد از SWAP چه MOVE)
        self.position += 1
        self.move_count += 1

    # ---------- اجرای حلقه اصلی ----------
    def run(self, max_passes=15):
        print("=" * 58)
        print("  عامل واکنشی ساده — مرتب‌سازی وزن (کوچک→بزرگ)")
        print("=" * 58)
        print(f"\nوضعیت اولیه خط ({self.env.n} جرم):")
        print(self.env.render())
        print(f"\nهدف: مرتب‌سازی صعودی بر اساس وزن")

        for _ in range(max_passes):
            self.pass_count += 1
            swaps_before = self.swap_count
            print(f"\n───────── چرخه {self.pass_count} ─────────")

            # عبور از کل خط
            while self.position < self.env.n - 1:
                current, neighbor = self.perceive()          # ادراک
                action = self.match_rules(current, neighbor) # تطبیق قانون

                if action == "SWAP":
                    print(f"  pos={self.position}: "
                          f"{current} > {neighbor} → SWAP")
                self.act(action)                             # اقدام

            # پایان چرخه → بازگشت به ابتدای خط
            print(f"  انتهای خط → RETURN")
            print(f"  خط: {self.env.render()}")

            # قانون ۴: بررسی پایان
            if self.swap_count == swaps_before:
                print(f"\n✅ در این چرخه هیچ تبادلی نشد — مرتب‌سازی تمام")
                break
            self.position = 0
        else:
            print("\n❌ به سقف چرخه‌ها رسید")

        print(f"\nنتیجه نهایی: {self.env.render()}")
        print(f"مرتب شده: {'✅ بله' if self.env.is_sorted() else '❌ خیر'}")
        print(f"آمار: چرخه={self.pass_count} | تبادل={self.swap_count} | "
              f"حرکت={self.move_count}")


if __name__ == "__main__":
    random.seed(42)
    env = LinearEnvironment(WEIGHTS)
    agent = SimpleReflexSorterAgent(env)
    agent.run()
