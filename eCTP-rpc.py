'''Copyright (C) 2020, ImPurpl3 - This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.'''

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
