import sdl2, sdl2.ext
from enum import Enum

class Type:
  ABSTRACT = 0
  UNKNOWN = 1
  ENTITY = 2

class EntityType:
  ABSTRACT = 0
  
  # NONLIVING
  NONLIVING_ABSTRACT = 1

  # LIVING
  LIVING_ABSTRACT = 2

