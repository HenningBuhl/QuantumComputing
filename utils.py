class dotdict(dict):
    def __init__(self, *args, **kwargs):
        super(dotdict, self).__init__(*args, **kwargs)
        for key, value in self.items():  # Add dict (key, value) as attributes.
            setattr(self, key, value)
