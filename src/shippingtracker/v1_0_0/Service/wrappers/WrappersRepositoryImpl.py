from .WrappersRepository import WrappersRepository
from shippingtracker.v1_0_0.Container.models.request.TrackRequest import TrackRequest
from shippingtracker.v1_0_0.Container.models.response.TrackResponse import TrackResponse
from shippingtracker.v1_0_0.Transformer.TrackTransformer import TrackTransformer
from shippingtracker.v1_0_0.Engine.repository.TrackingRepository import TrackingRepository


class WrappersRepositoryImpl(WrappersRepository):
    def __init__(self):
        self.trackTF = TrackTransformer()
        self.trackingRepository = TrackingRepository()

    def tracking(self, trackRequest: TrackRequest)->TrackResponse:
        return self.trackTF.getResponse(self.trackingRepository.save(self.trackTF.getEntity(trackRequest)))
        