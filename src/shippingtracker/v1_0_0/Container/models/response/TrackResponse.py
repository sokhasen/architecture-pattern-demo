class TrackResponse(object):
    
    def __init__(self, slug=None, tracking_number=None, created_at=None, updated_at=None,  data=[]):
        super().__init__()
        self.slug = slug
        self.tracking_number = tracking_number
        self.created_at = created_at
        self.updated_at = updated_at
        self.data = data

    @classmethod
    def fromdict(cls, adict):
        return TrackResponse(
            slug=adict["slug"],
            tracking_number=adict["tracking_number"],
            created_at=adict["created_at"],
            updated_at=adict["updated_at"],
            data=adict["data"],
        )
    
    def todict(self):
        return self.__dict__
    
        