from abc import ABC
from shippingtracker.v1_0_0.Container.models.request.TrackRequest import TrackRequest
from shippingtracker.v1_0_0.Container.models.response.TrackResponse import TrackResponse
class WrappersRepository(ABC):
    def tracking(self, trackRequest: TrackRequest) -> TrackResponse:
        raise NotImplementedError("{}:{}".format(self.__class__.__name__, " tracking method must implement!"))