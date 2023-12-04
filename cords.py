class Cords:
  def __init__(self, lon = '', lat = ''):
    self._lon = lon
    self._lat = lat

  def get_lat(self):
        return self._lat
    
  def get_lon(self):
        return self._lon
      
  def set_lat(self, latitude):
        self._lat = latitude
    
  def set_lon(self, longitude):
        self._lon = longitude