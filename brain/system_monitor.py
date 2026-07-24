import platform
import psutil


class SystemMonitor:


    def __init__(self):

        self.system = platform.system()

        self.machine = platform.machine()



    def get_status(self):

        cpu = psutil.cpu_percent(
            interval=None
        )


        memory = psutil.virtual_memory()


        disk = psutil.disk_usage(
            "/"
        )


        battery = psutil.sensors_battery()



        if battery:

            battery_text = (
                f"{battery.percent}%"
            )


            charging = (
                "charging"
                if battery.power_plugged
                else "not charging"
            )

        else:

            battery_text = "unavailable"

            charging = "unknown"



        return {

            "system": self.system,

            "machine": self.machine,

            "cpu": round(cpu),

            "ram": round(memory.percent),

            "disk": round(disk.percent),

            "battery": battery_text,

            "charging": charging

        }



    def spoken_status(self):

        data = self.get_status()


        return (
            "System diagnostics complete. "
            f"CPU {data['cpu']} percent. "
            f"Memory {data['ram']} percent. "
            f"Storage {data['disk']} percent. "
            f"Battery {data['battery']}."
        )



monitor = SystemMonitor()
