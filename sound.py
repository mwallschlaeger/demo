
import collections
import sys

import numpy as np
import sounddevice as sd

import colors

duration = 1000 #in seconds

BAR_COLOR_SCHEMA = {
35: {
    "color": colors.CGREEN2,
    "char": "|"
  },
45:{
    "color": colors.CYELLOW,
    "char": "|"
  }, 
55: {
    "color": colors.CRED,
    "char": "|"
  }
}


def audio_callback(indata, frames, time, status):
  volume_norm = np.linalg.norm(indata) * 10
  vn_i = int(volume_norm)

  s = ""
  chars = 0
  for k in list(BAR_COLOR_SCHEMA.keys()):
    if vn_i < k:
      s += BAR_COLOR_SCHEMA[k]["color"] + (BAR_COLOR_SCHEMA[k]["char"] * (vn_i - chars))
      break
    else:
      s += BAR_COLOR_SCHEMA[k]["color"] + (BAR_COLOR_SCHEMA[k]["char"] * (k - chars))
      chars = k
  print(s)


def main() -> int:
  stream = sd.InputStream(callback=audio_callback)
  with stream:
    sd.sleep(duration * 1000)

if __name__ == '__main__':
    sys.exit(main()) 