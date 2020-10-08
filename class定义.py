import time


class foo:
    def bar(self):
        if self=="True" or self=="0":
            print(self,".")
            time.sleep(0.1)
        else:
            print(self)
            time.sleep(0.2)

    def hello(self,name):
        time.sleep(0.3)
        print("My name is", name)


ass=foo
ass.bar("hello")
time.sleep(0.2)
ass.hello(True, "Li Jin yue")
