'''
Sahil Code for QRS peak detection
'''
class PanTompkins:
    def __init__(self, sampling_rate:int):
        self.sampling_rate = sampling_rate

    def step(self, ecg_signal:list[float]) -> bool:
        '''
        :param ecg_signal: Voltage value from ecg signal
        :return: True if QRS complex/ heart beat is detected, False otherwise
        '''
        # TODO: Implement QRS peak detection
        return False
