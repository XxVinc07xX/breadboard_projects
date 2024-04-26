#autor : XxVinc07xX

from gpiozero import LED
import time
import datetime

led_hour_1 = LED(23)
led_hour_2 = LED(18)
led_hour_3 = LED(15)
led_hour_4 = LED(14)
led_hour_5 = LED(17)

led_min_1 = LED(11)
led_min_2 = LED(24)
led_min_3 = LED(5)
led_min_4 = LED(6)
led_min_5 = LED(13)
led_min_6 = LED(19)

led_sec_1 = LED(25)
led_sec_2 = LED(12)
led_sec_3 = LED(16)
led_sec_4 = LED(26)
led_sec_5 = LED(20)
led_sec_6 = LED(21)



def bin_to_led(bin_string,seq):
    for i in range(len(bin_string), 0, -1):
        led_name = f"led_{seq}_{len(bin_string) - i + 1}"
        led = globals()[led_name] 
        if bin_string[i - 1] == '1':  
            led.on()
        else:
            led.off()


def led_off(seq):
    if (seq=="hour"):
        for i in range(5):
            led_name = f"led_{seq}_{i+1}"
            led = globals()[led_name]
            led.off()
    else:
        for i in range(6):
            led_name = f"led_{seq}_{i+1}"
            led = globals()[led_name]
            led.off()





if __name__ == "__main__":
    while (True):
        now = datetime.datetime.now().time()

        now_hours_int = now.hour
        now_hours_bin_brut = bin(now_hours_int)
        now_hours_bin = now_hours_bin_brut[now_hours_bin_brut.index('b')+1:]
        bin_to_led(now_hours_bin,"hour")
        if (now_hours_int == 0):
            led_off("hour")

        now_min_int = now.minute
        now_min_bin_brut = bin(now_min_int)
        now_min_bin = now_min_bin_brut[now_min_bin_brut.index('b')+1:]
        bin_to_led(now_min_bin,"min")
        if (now_min_int == 0):
            led_off("min")

        now_sec_int = now.second
        now_sec_bin_brut = bin(now_sec_int)
        now_sec_bin = now_sec_bin_brut[now_sec_bin_brut.index('b')+1:]
        bin_to_led(now_sec_bin,"seq")
        if (now_sec_int == 0):
            led_off("sec")

        #print(now_hours_int, now_min_int, now_sec_int)
        time.sleep(1)
