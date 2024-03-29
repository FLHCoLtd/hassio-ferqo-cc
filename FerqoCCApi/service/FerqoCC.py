class FerqoCC():
    def __init__(self, data):
        self.name =  data["name"] if "name" in data else "none"
        self.node_id = data["node_id"] if "node_id" in data else "none"
        self.type = data["HAtype"] if "type" in data else "none"
        self.status = data["status"] if "status" in data else "none"
        self.powerNow = data["powerNow"] if "powerNow" in data else "none"
        self.powerTotal = data["powerTotal"] if "powerTotal" in data else "none"
        self.extension_gateway = data["extension_gateway"] if "extension_gateway" in data else "none"
        self.temperature = data["temperature"] if "temperature" in data else "none"
        self.Manufacturer = data["Manufacturer"] if "Manufacturer" in data else "none"
        self.product = data["product"] if "product" in data else "none"
        self.battery = data["battery"] if "battery" in data else "none"
        self.AccelerationXaxis = data["Acceleration X-axis"] if "Acceleration X-axis" in data else "none"
        self.AccelerationYaxis = data["Acceleration Y-axis"] if "Acceleration Y-axis" in data else "none"
        self.AccelerationZaxis = data["Acceleration Z-axis"] if "Acceleration Z-axis" in data else "none"
        self.sensorStatus = data["sensorStatus"] if "sensorStatus" in data else "none"
        self.actionStatus = data["actionStatus"] if "actionStatus" in data else "none"
        self.color = data["color"] if "color" in data else "none"
        self.humidity = data["humidity"] if "humidity" in data else "none"
        self.pm25 = data["pm2.5"] if "pm2.5" in data else "none"
        self.co2 = data["co2"] if "co2" in data else "none"
        self.lux = data["lux"] if "lux" in data else "none"
        self.SeismicIntensity = data["Seismic Intensity"] if "Seismic Intensity" in data else "none"
