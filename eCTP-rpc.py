from pypresence import Presence
import time
import sty
from sty import fg, RgbFg

client_id = '786012261964709888'
RPC = Presence(client_id)
RPC.connect()

fg.set_style('statSet', RgbFg(66, 135, 245))
stat = fg.statSet + 'Status Set!'

fg.set_style('startUp', RgbFg(57, 230, 106))
start = fg.startUp + 'Starting Up!'

print(start)
time.sleep(1)

RPC.update(state="Receiving Therapy",details="eCrew Therapy Program" ,large_image="cus_up", large_text="HIM", small_image="fail", small_text="Failure")
print(stat)

while True:
    time.sleep(1)