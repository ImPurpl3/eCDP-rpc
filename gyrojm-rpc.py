import pypresence
from pypresence import Presence
import time

client_id = '790284462596161536'
RPC = Presence(client_id)
RPC.connect()

print('Starting Up')
time.sleep(1)

RPC.update(state="Beating GYROJM",details="GYROJM" ,large_image="gyrojm", large_text="GYROJM", small_image="server", small_text="wiimmfi")
print('Status Set!')

while True:
    time.sleep(1)