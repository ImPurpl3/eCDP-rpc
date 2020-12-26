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
