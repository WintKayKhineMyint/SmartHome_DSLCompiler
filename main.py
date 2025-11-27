import json

# devices we support
devices = {
    "led_light": "off",
    "blinder": "close",
    "tv": "off",
    "fan": "off",
    "door": "locked",
    "thermostat": "off",
    "stove": "off",
    "cctv": "off",
}


def execute(event=None, time=None):
    if time is not None and 6.00 <= time < 10.00:
        devices["led_light"] = "on"
        devices["thermostat"] = "on"
        devices["bliner"] = "open"

    if event == "start_cooking":
        devices["stove"] = "on"

    if time is not None and 22.00 <= time < 24.00:
        devices["led_light"] = "on"
        devices["blinder"] = "closed"
        devices["tv"] = "off"
        devices["speaker"] = "off"
        devices["cctv"] = "on"
        devices["door"] = "locked"

    if event == "movie_time":
        devices["tv"] = "on"
        devices["led_light"] = "off"
        devices["blinder"] = "closed"
        devices["thermostat"] = "on"

    if event == "away":
        devices["tv"] = "off"
        devices["led_light"] = "off"
        devices["stove"] = "off"
        devices["thermostat"] = "off"
        devices["washer"] = "off"
        devices["door"] = "locked"
        devices["blinder"] = "closed"
        devices["cctv"] = "on"


def save():
    with open("devices.json", "w") as f:
        json.dump(devices, f, indent=4)


print("\n Morning")
execute(time=7.00)
