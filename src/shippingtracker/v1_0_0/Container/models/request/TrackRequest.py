class TrackRequest(object):
    
    def __init__(self, slug=None, tracking_number=None):
        super().__init__()
        self.slug = slug
        self.tracking_number = tracking_number

    @classmethod
    def fromdict(cls, adict):
        # do validation with 
        return TrackRequest(
            slug=adict["slug"],
            tracking_number=adict["tracking_number"]
        )
    
    def todict(self) -> dict:
        return dict(slug=self.slug, tracking_number=self.tracking_number)

    
        