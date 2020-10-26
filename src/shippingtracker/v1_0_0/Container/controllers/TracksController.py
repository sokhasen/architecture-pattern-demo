from shippingtracker.v1_0_0.Container.models.request.TrackRequest import TrackRequest
from shippingtracker.v1_0_0.Container.models.response.TrackResponse import TrackResponse
from shippingtracker.v1_0_0.Service.wrappers.WrappersRepositoryImpl import WrappersRepositoryImpl

class TracksController(object):
    def __init__(self):
        super().__init__()
        self.wrappersSV = WrappersRepositoryImpl()

    def tracking(self, trackRequest: TrackRequest) ->TrackResponse:
        trackRequest = TrackRequest(
            slug = trackRequest.slug,
            tracking_number = trackRequest.tracking_number
        )
        return self.wrappersSV.tracking(trackRequest)
        