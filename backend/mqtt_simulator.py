# import threading
# import time
# import random

# def simulate_device_communication():
#     while True:
#         print("[MQTT] Simulating device data...")
#         time.sleep(5)

# def run_simulator():
#     thread = threading.Thread(target=simulate_device_communication)
#     thread.daemon = True
#     thread.start()


import threading
import time
import random

def simulate_device_data_publish():
    publisher = mqtt.Client()
    publisher.connect(MQTT_BROKER, MQTT_PORT, 60)
    publisher.loop_start()

    devices = ["Light", "Fan", "Heater", "AC"]
    while True:
        device = random.choice(devices)
        state = random.choice(["ON", "OFF"])
        msg = f"{device}:{state}"
        publisher.publish(TOPIC, msg)
        print(f"[SIMULATED MQTT] Sent: {msg}")
        time.sleep(5)

if __name__ == "__main__":
    start_mqtt()
    threading.Thread(target=simulate_device_data_publish, daemon=True).start()
    while True:
        time.sleep(1)
