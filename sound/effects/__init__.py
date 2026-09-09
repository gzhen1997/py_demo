print("init.py")

# 这表示当你使用from sound.effects import *这种用法时，你只会导入包里面这三个子模块。
__all__ = ["echo", "surround", "reverse"]
