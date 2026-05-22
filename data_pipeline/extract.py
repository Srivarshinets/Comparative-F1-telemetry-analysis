import fastf1
import os

os.makedirs('../data', exist_ok=True)

fastf1.Cache.enable_cache('../cache')

session = fastf1.get_session(2024,"Suzuka","Q")
session.load()

laps = session.laps

ver = laps.pick_driver("VER").pick_fastest()
lec = laps.pick_driver("LEC").pick_fastest()

ver_tel = ver.get_car_data().add_distance()
lec_tel = lec.get_car_data().add_distance()

ver_tel.to_csv('../data/ver_tel.csv',index=False)
lec_tel.to_csv('../data/lec_tel.csv',index=False)

print("Telemetry exported.")