import os

WIDTH = 400
HEIGHT = 500
FPS = 60
HIGHSCORE_FILE = "highscore.txt"

COLORS = {0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
          'lightText': (249, 246, 242),
          'darkText': (119, 110, 101),
          'other': (0, 0, 0),
          'bg': (187, 173, 160)}

def load_highscore():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as f:
            try:
                return int(f.read())
            except ValueError:
                return 0
    return 0

def save_highscore(highscore):
    with open(HIGHSCORE_FILE, "w") as f:
        f.write(str(highscore))