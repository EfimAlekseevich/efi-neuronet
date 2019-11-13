from core.dendrite import simple_dendrite
from core.drive import simple_drive
from samples import normalizers
from copy import deepcopy


class Neuron:

    def __init__(self, bias=0, num_dendrites=1,
                 drive=simple_drive,
                 dendrite_model=simple_dendrite,
                 activation_func=normalizers.simple_proportional):

        self.bias = bias
        self.drive = drive
        self.num_dendrites = num_dendrites
        self.dendrites = [deepcopy(dendrite_model) for _ in range(num_dendrites)]
        self.activation_func = activation_func

    def __str__(self):
        return 'NEURON'

    def process_signals(self, in_signals):
        Neuron.check_warnings(self.num_dendrites, len(in_signals))
        signal_sum = self.get_sum(in_signals)
        out_signal = self.activation_func(self.drive.process_signal(signal_sum))
        return out_signal

    def get_sum(self, in_signals):
        signal_sum = self.bias
        for index in range(min(self.num_dendrites, len(in_signals))):
            dendrite = self.dendrites[index]
            signal = in_signals[index]
            signal_sum += dendrite.process_signal(signal)
        return signal_sum

    @classmethod
    def check_warnings(cls, num_inputs, num_input_signals):
        message = None
        if num_input_signals < num_inputs:
            message = f'Number of input signals {num_input_signals} more then number of inputs {num_inputs}.'
        elif num_input_signals > num_inputs:
            message = f'Number of input signals {num_input_signals} less then number of inputs {num_inputs}.'

        if message:
            print(f'WARNING: {message}\n')
