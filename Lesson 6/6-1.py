from time import sleep
import colorama
import sys

colorama.init()


class Colortraffic:
    def start(self):
        while True:
            print(f"\r\033[31m{chr(11035)}", end="")
            sleep(7)
            print(f"\r\033[30m{chr(11035)}")
            print(f"\r\033[33m{chr(11035)}", end="")
            sleep(2)
            print(f"\r\033[30m{chr(11035)}")
            print(f"\r\033[32m{chr(11035)} ", end="")
            sleep(4)
            print(f"\r\033[30m{chr(11035)}", end="")
            sys.stdout.write("\r\x1b[2A")


color = Colortraffic()
color.start()
