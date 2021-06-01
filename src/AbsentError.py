class AbsentError(Exception):
   def __init__(self):
       pass

   def __str__(self):
      return 'Absence of a required parameter'