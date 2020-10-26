class TrackEntity(object):
    def __init__(self, slug=None, tracking_number=None):
        super(TrackEntity, self).__init__()
        self.slug = slug
        self.tracking_number = tracking_number
        