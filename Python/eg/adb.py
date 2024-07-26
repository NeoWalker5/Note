import os
import time

# 定义应用包名和Activity名称
package_name = "com.serenasecret.mergegame"
activity_name = ".MainActivity"

# 打开应用
os.system(f"adb shell am start -n {package_name}/{activity_name}")

# 等待10秒
time.sleep(10)

# 关闭应用
os.system(f"adb shell am force-stop {package_name}")

# 再次打开应用
os.system(f"adb shell am start -n {package_name}/{activity_name}")
