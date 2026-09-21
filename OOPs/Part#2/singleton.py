class logger:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            print("logger created!")
            cls._instance= super().__new__(cls)
        return cls._instance

    def log(self,message):
        print(f"[log]:{message}")

c = logger()
c.log("App started")

# c2 = logger()
# c2.log("App running")

