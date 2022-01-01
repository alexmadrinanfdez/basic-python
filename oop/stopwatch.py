import time

class Stopwatch:
    # create and start a stop watch
    def __init__(self):
        self._start = time.time()
    
    # returns elapsed time since stopwatch was started
    def lap(self, unit='ms'):
        if(unit == 'ms'):
            return (time.time() - self._start) * 1000
        elif(unit == 's'):
            return (time.time() - self._start)
        else:
            return ValueError("Valid units are seconds and milliseconds only.")

if __name__ == "__main__":
    import sys
    sw = Stopwatch()
    secs = float(sys.argv[1])

    time.sleep(secs)

    print("Elapsed time (in seconds) is", sw.lap(unit='s'))