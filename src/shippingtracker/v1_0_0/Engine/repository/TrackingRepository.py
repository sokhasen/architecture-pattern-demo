from shippingtracker.v1_0_0.Engine.entity.TrackEntity import TrackEntity
from shippingtracker.v1_0_0.Container.models.response.TrackResponse import TrackResponse
import datetime
from random import random, gauss
class TrackingRepository(object):
    def __init__(self):
        super(TrackingRepository, self).__init__()
    
    def save(self, trackEntity: TrackEntity) -> TrackResponse:
        print("Save data from wrappers to DB.....")
        
        now =datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
        return TrackResponse(
            slug=trackEntity.slug,
            tracking_number=trackEntity.tracking_number,
            created_at=now,
            updated_at=now,
            data= [gauss(0, 100), gauss(0, 100), gauss(0, 100), gauss(0, 100), gauss(0, 100)]
        )
        