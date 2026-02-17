import RPi.GPIO as GPIO
import time

class R2R_DAC:
    def __init__(self, vref):
        self.vref = vref
        self.leds = [16, 12, 25, 17, 27, 23, 22, 24]
        GPIO.setup(self.leds, GPIO.OUT)
        GPIO.output(self.leds, 0)
    
    def set_value(self, value):
        bits = [int(bit) for bit in bin(value)[2:].zfill(8)]
        GPIO.output(self.leds, bits)
    
    def __del__(self):
        GPIO.output(self.leds, 0)

class R2R_ADC:
    def __init__(self, vref):
        self.vref = vref
        self.leds = [16, 12, 25, 17, 27, 23, 22, 24]
        self.comp_pin = 26
        self.dac = R2R_DAC(vref)
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.leds, GPIO.OUT)
        GPIO.setup(self.comp_pin, GPIO.IN)
        GPIO.output(self.leds, 0)
    
    def successive_approximation_adc(self):
        value = 0
        for bit in range(7, -1, -1):
            test_value = value | (1 << bit)
            self.dac.set_value(test_value)
            time.sleep(0.001)
            
            if GPIO.input(self.comp_pin) == 1:
                value = test_value
        
        return value
    
    def get_sar_voltage(self):
        value = self.successive_approximation_adc()
        return (value / 255) * self.vref
    
    def __del__(self):
        GPIO.output(self.leds, 0)

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.3)
        while True:
            voltage = adc.get_sar_voltage()
            print(f"Voltage: {voltage:.3f} V")
            time.sleep(0.5)
    finally:
        GPIO.cleanup()