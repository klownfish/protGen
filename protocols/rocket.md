GENERATED FILE DO NOT EDIT

# rocket - Description
## All messages
<table>
<thead>
<tr>
<th>ID</th>
<th>sender</th>
<th>receiver</th>
<th>name</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>local</td>
<td>local</td>
<td>local_timestamp</td>
</tr>
<tr>
<td>1</td>
<td>rocket</td>
<td>ground</td>
<td>timestamp</td>
</tr>
<tr>
<td>2</td>
<td>ground</td>
<td>rocket</td>
<td>handshake</td>
</tr>
<tr>
<td>3</td>
<td>rocket</td>
<td>ground</td>
<td>handshake</td>
</tr>
<tr>
<td>4</td>
<td>ground</td>
<td>rocket</td>
<td>simple_calibration</td>
</tr>
<tr>
<td>5</td>
<td>ground</td>
<td>rocket</td>
<td>mag_calibration</td>
</tr>
<tr>
<td>6</td>
<td>ground</td>
<td>rocket</td>
<td>wipe_flash</td>
</tr>
<tr>
<td>7</td>
<td>ground</td>
<td>rocket</td>
<td>play_music</td>
</tr>
<tr>
<td>8</td>
<td>ground</td>
<td>rocket</td>
<td>set_logging</td>
</tr>
<tr>
<td>9</td>
<td>ground</td>
<td>rocket</td>
<td>dump_flash</td>
</tr>
<tr>
<td>10</td>
<td>rocket</td>
<td>ground</td>
<td>flash_address</td>
</tr>
<tr>
<td>11</td>
<td>rocket</td>
<td>ground</td>
<td>bmp</td>
</tr>
<tr>
<td>12</td>
<td>rocket</td>
<td>ground</td>
<td>mpu</td>
</tr>
<tr>
<td>13</td>
<td>rocket</td>
<td>ground</td>
<td>battery_voltage</td>
</tr>
<tr>
<td>14</td>
<td>ground</td>
<td>rocket</td>
<td>set_state</td>
</tr>
<tr>
<td>15</td>
<td>rocket</td>
<td>ground</td>
<td>state</td>
</tr>
<tr>
<td>16</td>
<td>rocket</td>
<td>ground</td>
<td>rssi</td>
</tr>
<tr>
<td>17</td>
<td>relay</td>
<td>ground</td>
<td>rssi</td>
</tr>
<tr>
<td>18</td>
<td>rocket</td>
<td>ground</td>
<td>ms_since_boot</td>
</tr>
</tbody>
</table>

### 0 - local_timestamp <br> local &rarr; local
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>local_timestamp</td>
<td>uint</td>
<td>uint32</td>
<td>N/A</td>
</tr>
</tbody>
</table>

### 1 - timestamp <br> rocket &rarr; ground
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>ms_since_boot</td>
<td>uint</td>
<td>uint32</td>
<td>N/A</td>
</tr>
</tbody>
</table>

### 2 - handshake <br> ground &rarr; rocket
*empty*
### 3 - handshake <br> rocket &rarr; ground
*empty*
### 4 - simple_calibration <br> ground &rarr; rocket
*empty*
### 5 - mag_calibration <br> ground &rarr; rocket
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>declination</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
</tbody>
</table>

### 6 - wipe_flash <br> ground &rarr; rocket
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>this_to_42</td>
<td>uint</td>
<td>uint8</td>
<td>N/A</td>
</tr>
</tbody>
</table>

### 7 - play_music <br> ground &rarr; rocket
*empty*
### 8 - set_logging <br> ground &rarr; rocket
#### bits
<table>
<thead>
<tr>
<th>bit</th>
<th>name</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>is_enabled</td>
</tr>
</tbody>
</table>

### 9 - dump_flash <br> ground &rarr; rocket
*empty*
### 10 - flash_address <br> rocket &rarr; ground
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>address</td>
<td>uint</td>
<td>uint32</td>
<td>N/A</td>
</tr>
</tbody>
</table>

### 11 - bmp <br> rocket &rarr; ground
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>altitude</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>temperature</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
</tbody>
</table>

### 12 - mpu <br> rocket &rarr; ground
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>acc_x</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>acc_y</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>acc_z</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>gyro_x</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>gyro_y</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>gyro_z</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>mag_x</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>mag_y</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>mag_z</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
</tbody>
</table>

### 13 - battery_voltage <br> rocket &rarr; ground
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>voltage</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
</tbody>
</table>

### 14 - set_state <br> ground &rarr; rocket
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>state</td>
<td>enum</td>
<td>uint8</td>
<td>enum=state</td>
</tr>
</tbody>
</table>

### 15 - state <br> rocket &rarr; ground
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>state</td>
<td>enum</td>
<td>uint8</td>
<td>enum=state</td>
</tr>
</tbody>
</table>

### 16 - rssi <br> rocket &rarr; ground
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>rssi</td>
<td>scaledFloat</td>
<td>int16</td>
<td>scale=100</td>
</tr>
</tbody>
</table>

### 17 - rssi <br> relay &rarr; ground
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>rssi</td>
<td>scaledFloat</td>
<td>int16</td>
<td>scale=100</td>
</tr>
</tbody>
</table>

### 18 - ms_since_boot <br> rocket &rarr; ground
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>ms_since_boot</td>
<td>uint</td>
<td>uint32</td>
<td>N/A</td>
</tr>
</tbody>
</table>

## Enums
### state
<table>
<thead>
<tr>
<th>name</th>
<th>value</th>
</tr>
</thead>
<tbody>
<tr>
<td>sleeping</td>
<td>0</td>
</tr>
<tr>
<td>awake</td>
<td>1</td>
</tr>
<tr>
<td>ready</td>
<td>2</td>
</tr>
<tr>
<td>ascending</td>
<td>3</td>
</tr>
<tr>
<td>falling</td>
<td>4</td>
</tr>
<tr>
<td>landed</td>
<td>5</td>
</tr>
</tbody>
</table>

### nodes
<table>
<thead>
<tr>
<th>name</th>
<th>value</th>
</tr>
</thead>
<tbody>
<tr>
<td>local</td>
<td>0</td>
</tr>
<tr>
<td>rocket</td>
<td>1</td>
</tr>
<tr>
<td>ground</td>
<td>2</td>
</tr>
<tr>
<td>relay</td>
<td>3</td>
</tr>
</tbody>
</table>

### fields
<table>
<thead>
<tr>
<th>name</th>
<th>value</th>
</tr>
</thead>
<tbody>
<tr>
<td>local_timestamp</td>
<td>0</td>
</tr>
<tr>
<td>ms_since_boot</td>
<td>1</td>
</tr>
<tr>
<td>declination</td>
<td>2</td>
</tr>
<tr>
<td>this_to_42</td>
<td>3</td>
</tr>
<tr>
<td>is_enabled</td>
<td>4</td>
</tr>
<tr>
<td>address</td>
<td>5</td>
</tr>
<tr>
<td>altitude</td>
<td>6</td>
</tr>
<tr>
<td>temperature</td>
<td>7</td>
</tr>
<tr>
<td>acc_x</td>
<td>8</td>
</tr>
<tr>
<td>acc_y</td>
<td>9</td>
</tr>
<tr>
<td>acc_z</td>
<td>10</td>
</tr>
<tr>
<td>gyro_x</td>
<td>11</td>
</tr>
<tr>
<td>gyro_y</td>
<td>12</td>
</tr>
<tr>
<td>gyro_z</td>
<td>13</td>
</tr>
<tr>
<td>mag_x</td>
<td>14</td>
</tr>
<tr>
<td>mag_y</td>
<td>15</td>
</tr>
<tr>
<td>mag_z</td>
<td>16</td>
</tr>
<tr>
<td>voltage</td>
<td>17</td>
</tr>
<tr>
<td>state</td>
<td>18</td>
</tr>
<tr>
<td>rssi</td>
<td>19</td>
</tr>
</tbody>
</table>

### messages
<table>
<thead>
<tr>
<th>name</th>
<th>value</th>
</tr>
</thead>
<tbody>
<tr>
<td>local_timestamp</td>
<td>0</td>
</tr>
<tr>
<td>timestamp</td>
<td>1</td>
</tr>
<tr>
<td>handshake</td>
<td>2</td>
</tr>
<tr>
<td>simple_calibration</td>
<td>3</td>
</tr>
<tr>
<td>mag_calibration</td>
<td>4</td>
</tr>
<tr>
<td>wipe_flash</td>
<td>5</td>
</tr>
<tr>
<td>play_music</td>
<td>6</td>
</tr>
<tr>
<td>set_logging</td>
<td>7</td>
</tr>
<tr>
<td>dump_flash</td>
<td>8</td>
</tr>
<tr>
<td>flash_address</td>
<td>9</td>
</tr>
<tr>
<td>bmp</td>
<td>10</td>
</tr>
<tr>
<td>mpu</td>
<td>11</td>
</tr>
<tr>
<td>battery_voltage</td>
<td>12</td>
</tr>
<tr>
<td>set_state</td>
<td>13</td>
</tr>
<tr>
<td>state</td>
<td>14</td>
</tr>
<tr>
<td>rssi</td>
<td>15</td>
</tr>
<tr>
<td>ms_since_boot</td>
<td>16</td>
</tr>
</tbody>
</table>

### categories
<table>
<thead>
<tr>
<th>name</th>
<th>value</th>
</tr>
</thead>
<tbody>
<tr>
<td>none</td>
<td>0</td>
</tr>
</tbody>
</table>

