
class Node:
  def __init__(self, value, address = None):
    self.value = value
    self.address = address
    
  def set_next_node(self, address):
    self.address = address
    
  def get_next_node(self):
    return self.address
  
  def get_value(self):
    return self.value
