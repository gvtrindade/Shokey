import json

class SerialData():
  def __init__(self, json_string):
    self.app = None
    self.action = None
    self.data = None

    self.extract_serial_data(json_string)

  def extract_serial_data(self, json_string):
    data = json.loads(json_string)
    self.app = data['app']
    self.action = data['action']
    self.data = data['data']