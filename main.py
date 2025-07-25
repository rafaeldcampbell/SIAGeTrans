from controllers.databaseController import DatabaseController
from controllers.trafficLightController import TrafficLightController
import configs.configs as configs
from datetime import datetime
from models.databaseObject import DatabaseObject, EventType

databaseController = DatabaseController()


# ## Testing TrafficLightController
trafficlights = databaseController.getTrafficLightsAtIntersection(1)
trafficlightController = TrafficLightController(1, '24210', trafficlights)
trafficlightController.startManagement()



# ## Testing Select
# event = databaseController.select('events', 1)
# print(event.__dict__)

# ## Testing Insert
# event = DatabaseObject('events', id_eventtype = 1,
#                                 dt_start = datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
#                                 dt_creation = datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
#                                 dt_expiration = '', 
#                                 ds_comment =  'Teste',
#                                 es_status =  1)
# print(event.__dict__)
# print(databaseController.insert(event))
# print(event.__dict__)

# ## Testing Delete
# event = DatabaseObject('events', id=4)
# print(event.__dict__)
# print(databaseController.delete(event))

# ## Testing Update
# event = databaseController.select('events', 1)
# print(event.__dict__)
# event.id_eventtype = EventType.TOTAL_ROAD_CLOSURE.value
# print(event.__dict__)
# databaseController.update(event)
# event = databaseController.select('events', 1)
# print(event.__dict__)

