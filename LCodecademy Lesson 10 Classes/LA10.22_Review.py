class SortedList(list):
  pass

  def append(self, value):
     super().append(value)
     self.sort()

     
