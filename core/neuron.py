from core.dendrite import simple_dendrite
from core.drive import simple_drive
from samples import normalizers
from copy import deepcopy


class Neuron:

    def __init__(self, num_dendrites=0,
                 drive=simple_drive,
                 dendrite_model=simple_dendrite,
                 activation_func=normalizers.simple_proportional):

        self.drive = drive
        self.num_dendrites = num_dendrites
        self.dendrites = [deepcopy(dendrite_model) for _ in range(num_dendrites)]
        self.activation_func = activation_func

    def __str__(self):
        return 'NEURON'

    def process_signals(self, in_signals):
        signal_sum = self.get_sum(in_signals)
        out_signal = self.activation_func(self.drive.process_signal(signal_sum))
        return out_signal

    def get_sum(self, in_signals):
        signal_sum = 0
        for index in range(self.num_dendrites):
            dendrite = self.dendrites[index]
            signal = in_signals[index]
            signal_sum += dendrite.process_signal(signal)
        return signal_sum


bias_neuron = Neuron(activation_func=normalizers.bias)
simple_neuron = Neuron()
