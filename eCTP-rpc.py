from pypresence import Presence
import time

client_id = '786012261964709888'
RPC = Presence(client_id)
RPC.connect()

print(RPC.update(state="Receiving Therapy",details="eCrew Therapy Program" ,large_image="cus_up", large_text="HIM", small_image="fail", small_text="Failure"))

while True:
    time.sleep(1)