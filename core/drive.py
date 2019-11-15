import samples.stability
import samples.memory


class Drive:

    def __init__(self, memory_func=samples.memory.simple_proportional,
                 stability_func=samples.stability.stable, stability=0,
                 out_signal=0):
        self.memory_func = memory_func
        self.stability_func = stability_func
        self.stability = stability
        self.out_signal = out_signal

    def __str__(self):
        return 'DRIVE'

    def process_signal(self, in_signal=0, limiter=None):
        delta = in_signal - self.out_signal
        self.stability = self.stability_func(stability=self.stability, delta=delta, limiter=limiter)
        memory = self.memory_func(stability=self.stability)
        self.out_signal = self.out_signal + delta / memory
        return self.out_signal


simple_drive = Drive()
