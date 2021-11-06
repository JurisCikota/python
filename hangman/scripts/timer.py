
import time, os


class timer:
    def __init__(self):
        self.seconds_to_go_for = 10
        self.current_time = int(time.time())
    def clear(self):
        if os.name == "nt":
         os.system("cls")
        else:
         os.system("clear")    
    def time(self):
        while True:
            time_now = int(time.time())
            if time_now >= self.current_time + self.seconds_to_go_for:
             break

            print(f"Pagājušas sekundes:  {time_now - self.current_time}")
            self.clear()
        
        print("Laiks ir beidzies")





 