from core.drive import Drive, simple_drive, proportional_dynamic_limited_drive, exponential_dynamic_limited_drive


class BaseDendrite:

    def __init__(self, weight):
        self.weight = weight

    def __call__(self):
        return self.weight


class Dendrite(BaseDendrite):

    def __init__(self, weight=1, drive=simple_drive):
        super().__init__(weight)
        self.drive = drive

    def __str__(self):
        return f'DENDRITE || WEIGHT = {self.weight}'

    def process_signal(self, in_signal):
        out_signal = self.drive.process_signal(in_signal) * self.weight
        return out_signal


simple_dendrite = Dendrite(drive=simple_drive)
proportional_dynamic_limited_dendrite = Dendrite(drive=proportional_dynamic_limited_drive)
exponential_dynamic_limited_dendrite = Dendrite(drive=exponential_dynamic_limited_drive)
