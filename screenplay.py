from collections import OrderedDict


class Screenplay():

    INT_EXT = ['INT.', 'EXT.', 'INT/EXT.', 'EXT/INT.']
    TOD = ['AFTERNOON', 'CONTINUOUS', 'DAWN', 'DAY', 'DUSK',
           'EVENING', 'LATER', 'MORNING', 'NIGHT', 'NOON', 'SAME']
    TRANSITIONS = ['BACK TO:', 'CUT TO:', 'DISSOLVE TO:', 'FADE IN:', 'CUT BACK TO:'
                   'FADE OUT:', 'FADE TO:', 'JUMP CUT TO:', 'MATCH CUT TO:', 'TITLE:',
                   'SMASH CUT TO:', 'TIME CUT:', 'WIPE TO:', 'CROSSFADE:', 'OVER BLACK:', 'CUT TO BLACK',
                   'FADE TO:BLACK', 'FLASH CUT:', 'LAP DISSOLVE:', 'MATCH DISSOLVE TO:', 'SUPER:', 'IRIS OUT:']
    SHOTS = ['AERIAL SHOT', 'ANGLE ON',  'CLOSE ON', 'CLOSER ANGLE', 'CONTINUOUS',
             'CONTRAZOOM', 'CRAWL',  'ESTABLISHING SHOT', 'DAYS LATER'
             'EXTREMELY LONG SHOT (XLS):', 'FAVOR ON',
             'FLASHBACK:', 'FREEZE FRAME:', 'INSERT',
             'INTO FRAME:', 'INTO VIEW:', 'MOS', 'O.C. / O.S.',
             'POV', 'PULL BACK:', 'PULL FOCUS:', 'PUSH IN:',
             'REVERSE ANGLE',  'SPLIT SCREEN SHOT:', 'STOCK SHOT:',
             'TIGHT ON', 'TIME CUT', 'V.O.', 'ZOOM:']

    def __init__(self, text: list) -> dict:
        self.text = [l.strip() for l in text if not l.isspace()]

    def get_scenes(self):
        self.scenes = []
        for i in [e for e in self.text if e.isupper() and e not in self.TRANSITIONS]:
            for item in i.split():
                if item in self.INT_EXT:
                    scene = ' '.join([x for x in i.split()])
                    self.scenes.append(scene)
        return self.scenes

    def parse(self):
        scenes = {}

        for i, s in enumerate(self.get_scenes(),start=1):
            scenes.update({
                i: {
                    f'int_ext': [l for l in s.split()][0],
                    'location': ' '.join([l for l in s.split()][1:-2]),
                    'tod': [l for l in s.split()][-1]
                }})


if __name__ == '__main__':
    with open('text.txt', 'r') as f:
        text = f.readlines()

        sc = Screenplay(text)
        print(len(sc.get_scenes()))
