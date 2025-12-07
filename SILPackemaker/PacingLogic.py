class PacingLogic:
    def __init__(self, NBG_Code, sampling_rate):
        self.NBG_Code = NBG_Code
        self.sampling_rate = sampling_rate
        self.time_since_last_event = 0

    """Convert BPM to number of samples"""
    def _bpm_to_samples(self, bpm):
        interval_seconds = 60.0 / bpm
        return int(interval_seconds * self.sampling_rate)
    
    def step(self,is_heartbeat:bool, min_rate:int):
        target_sample_count = self._bpm_to_samples(min_rate)

        if is_heartbeat:
            self.time_since_last_event = 0
        else:
            self.time_since_last_event +=1

        if self.time_since_last_event >= target_sample_count:
            #Trigger a heartbeat
            self.time_since_last_event = 0 #reset
            return True # send an impulse to trigger a contraction
        return False
