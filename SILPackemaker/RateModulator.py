class RateModulator:
    def __init__(self, adaptive: bool, sampling_rate:int):
        self.adaption = adaptive
        self.prev_bpm = 60
        self.sampling_rate = sampling_rate

    def step(self, sensor_signal:int, min_bpm = 60, max_bpm = 140, max_delta = 3):
        '''
        In our case for adaptive pacing logic we're only implmenting linear pacing logic for simplificty 
        purposes but in reality pacing logic will likely be linear 
        
        :param sensor_signal: [0-100] value of sensor typically attached to heart 0- low exertion 100- max exertion
        :maxDelta = max change in bpm per second
        '''
        
        if self.adaption:
            def calculate_base_bpm(x:int):
                m = (max_bpm - min_bpm) / 100
                return m*x + min_bpm # y= mx+b for new linear heart rate
            
            max_delta_samping_rate = abs(max_delta) / self.sampling_rate 

            # calculate new bpm 
            new_bpm = calculate_base_bpm(sensor_signal)

            # calculated change in bpm 
            bpm_change  = new_bpm - self.prev_bpm

            # bpm_change is more than the delta that we need 
            if abs(bpm_change) > max_delta_samping_rate:
                if bpm_change < 0: 
                    bpm_change = -max_delta_samping_rate
                else: 
                    bpm_change = max_delta_samping_rate
                # Calculate the new_bpm from the clamped bpm _change
                new_bpm = self.prev_bpm + bpm_change 

            self.prev_bpm = new_bpm 
            return max(min_bpm, min(new_bpm, max_bpm)) # clamping
        else: 
            # fixed pace pacemaker
            self.prev_bpm = min_bpm 
            return min_bpm 
