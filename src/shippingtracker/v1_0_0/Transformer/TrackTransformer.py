from shippingtracker.v1_0_0.Engine.entity.TrackEntity import TrackEntity
from shippingtracker.v1_0_0.Container.models.request.TrackRequest import TrackRequest
from shippingtracker.v1_0_0.Container.models.response.TrackResponse import TrackResponse
class TrackTransformer(object):
    def getEntity(self, trackReq: TrackRequest)->TrackEntity:
        trackEntity = TrackEntity(
            slug=trackReq.slug,
            tracking_number=trackReq.tracking_number
        )
        return trackEntity

    def getResponse(self, trackEntity: TrackEntity)->TrackResponse:
        response = TrackResponse(
            slug=trackEntity.slug,
            tracking_number=trackEntity.tracking_number,
            created_at=trackEntity.created_at,
            updated_at=trackEntity.updated_at,
            data=trackEntity.data,
        )
        return response
