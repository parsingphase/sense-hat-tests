from sense_hat import SenseHat
sense = SenseHat()
from gpiozero import CPUTemperature

for o in range(0, 360 , 90):
    sense.set_rotation((o + 180) %360)
    temp = round(sense.get_temperature_from_humidity(),1)
    sense.show_message(f'{temp} C',text_colour=(0x44,0x44,0xff) )
    cpu = CPUTemperature()
    temp = round(cpu.temperature,1)
    sense.show_message(f'{temp} C',text_colour=(0x44,0xff,0x44) )
    humidity = round(sense.get_humidity(),1)
    sense.show_message(f'{humidity} %',text_colour=(0xff,0x44,0x44))
    pressure = sense.get_pressure()
    sense.show_message(f'{pressure} mb',text_colour=(0xff,0xff,0x44))
    print(sense.pressure)

sense.clear()