 import os

# Dump memory

cmd = "del mine.dmp"
os.system(cmd)
cmd = "procdump -ma minesam.exe mine"
os.system(cmd)

# Find gameboard

mark_exprt =  b'\x00\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x0F'
mark_intrm = b'\x00\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x0F'
mark_bgnr = b'\x00\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x0F'

line_length = 32
board_size = 0 # characters in whole board

with open("mine.dmp", "rb") as f:
  data= f.read()

start = 0
start_exprt = data.find(mark_exprt)
start_intrm = data.find(mark_intrm)
start_bgnr = data.find(mark_bgnr)
start_row = '   '
start_col = ' '

if start_intrm > 0:
  start = start_intrm
  board_size = 32 * 18
  start_row += '0123456789ABCDEF'
  start_col += '0123456789ABCDEF '
elif start_bgnr > 0:
  start = start_bgnr
  board_size = 32 * 11
  start_row += '012345678'
  start_col += '012345678 '
elif start_exprt > 0:
  start = start_exprt + 1
  board_size = 32 * 18
  start_row += '0123456789ABCDEFGHIJKLMNOPQRS'
  start_col += '0123456789ABCDEF '

# Print gameboard

print(start_row)
for i in range(0, board_size, line_length):
  line = ''
  line += start_col[(i//line_length)]
  for j in range(line_length):
    g = data[start+i+j]
    g = f"{g:02X}"
    if g == '10':
      c = "-"
    elif g == '0F':
      c = " "
    elif g == '8A' or g == 'CC' or g == '8F':
      c = "*"
    elif g == '00':
      c = " "
    elif g == '40':
      c = " "
    elif g == '41':
      c = "1"
    elif g == '42':
      c = "2"
    elif g == '43':
      c = "3"
    elif g == '44':
      c = "4"
    elif g == '45':
      c = "5"
    elif g == '46':
      c = "6"
    elif g == '47':
      c = "7"
    elif g == '48':
      c = "8"
    else:
      c = "I"
    line += c
  print(line)
