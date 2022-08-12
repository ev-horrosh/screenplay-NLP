from dataclasses import dataclass, field


@dataclass
class Screenplay:

    text: str

    result = {}

    INT_EXT: list[str] = field(default_factory=lambda: [
                               'INT.', 'EXT.', 'INT/EXT.', 'EXT/INT.'])
    TOD: list[str] = field(default_factory=lambda: ['AFTERNOON', 'CONTINUOUS', 'DAWN', 'DAY', 'DUSK',
                                                    'EVENING', 'LATER', 'MORNING', 'NIGHT', 'NOON', 'SAME', 'SUNSET'])

    TRANSITIONS: list[str] = field(init=True, default_factory=lambda: ['BACK TO:', 'CUT TO:', 'DISSOLVE TO:', 'FADE IN:', 'CUT BACK TO:', 'CUT BACK TO:',
                                                            'FADE OUT:', 'FADE TO:', 'JUMP CUT TO:', 'MATCH CUT TO:', 'TITLE:', 'QUICK CUTS:',
                                                            'SMASH CUT TO:', 'TIME CUT:', 'WIPE TO:', 'CROSSFADE:', 'OVER BLACK:', 'CUT TO BLACK',
                                                            'FADE TO:BLACK', 'FLASH CUT:', 'LAP DISSOLVE:', 'MATCH DISSOLVE TO:', 'SUPER:', 'IRIS OUT:'])
    SHOTS: list[str] = field(default_factory=lambda: ['AERIAL SHOT', 'ANGLE ON',  'CLOSE ON', 'CLOSER ANGLE', 'CONTINUOUS',
                                                      'CONTRAZOOM', 'CRAWL',  'ESTABLISHING SHOT',
                                                      'EXTREMELY LONG SHOT (XLS):', 'FAVOR ON', 'HEAR LAUGHTER.',
                                                      'FLASHBACK:', 'FREEZE FRAME:', 'INSERT', 'DAYS LATER'
                                                      'INTO FRAME:', 'INTO VIEW:', 'MOS', 'O.C. / O.S.',
                                                      'POV', 'PULL BACK:', 'PULL FOCUS:', 'PUSH IN:',
                                                      'REVERSE ANGLE',  'SPLIT SCREEN SHOT:', 'STOCK SHOT:',
                                                      'TIGHT ON', 'TIME CUT', 'V.O.', 'ZOOM:'])

    # def __post_init__(self):
    #     self.text = text

    @classmethod
    def read_txt(cls,file):
        with open (file,'r') as f:
            text=f.readlines()
            return cls(text)

    @classmethod
    def add_transition(cls, transition):
        cls.TRANSITIONS.append(transition)
        return cls(transition)

    
    def add_shot(self, shot):
        self.SHOTS.append(shot)

    def locations(self) -> list[str]:
        locations = []
        for i in [e.strip() for e in self.text if e.isupper() and e not in self.TRANSITIONS]:
            for item in i.split():
                if item in self.INT_EXT:
                    scene = ' '.join([x for x in i.split()])
                    locations.append(scene)
        return locations

    def scene_index(self):
        return [i for i, l in enumerate(self.text) if l.strip() in self.locations()]

    def scenes(self):
        scene_index = self.scene_index()
        result = {}
        for i, _ in enumerate(scene_index, 1):
            if scene_index[i-1] == scene_index[-1]:
                result.update({i: {'text': self.text[scene_index[i-1]:]}})
            else:
                result.update(
                    {i: {'text': self.text[scene_index[i-1]:scene_index[i]]}})
        return result

    def transitions(self):
        result = {}
        for i, v in enumerate(self.scenes().items(), start=1):
            result.update(
                {i: {'transitions': [t for t in v[1]['text'] if t in self.TRANSITIONS]}})
        return result

    def scene_att_extraction(self, text, scene_attribute):
        result = []
        for line in text:
            [result.append(t) for t in scene_attribute if t in line]
        return result

    def locsplit(self, text):
        temp = ' '.join([l for l in text.split() if l not in self.TOD][1:-1])

        def strip_dash(temp):
            if not temp.endswith('-'):
                return temp
            else:
                temp = temp.rstrip('- ')
                return strip_dash(temp)
        result = strip_dash(temp)
        return result

    def extract_dialogs(self, text):
        return [i.strip() for i in text if not i[15:25].strip() != '' and i[69:79] == '' and i != '\n']

    def character_dialog(self, dialog):
        result = {}
        dialog_index = []
        for i, d in enumerate([dialog]):
            [dialog_index.append(index)
             for index, t in enumerate(d) if t.isupper()]

        for i, t in enumerate(dialog_index):
            character = dialog[dialog_index[i]]
            try:
                if dialog_index[i] == dialog_index[-1]:
                    result[character] = result.get(
                        character, [])+dialog[dialog_index[i]+1:]
                else:
                    result[character] = result.get(
                        character, [])+dialog[dialog_index[i]+1:dialog_index[i+1]]
            except:
                result[character] = result.get(character, [])
        return result

    def extract_action(self, text):
        return [i.strip() for i in text if i[:16].strip() != '' and i.strip() not in self.locations()]

    def load(self):
        result = {}
        for i, s in enumerate(self.scenes().items(), start=1):

            result.update({
                i: {
                    'int_ext': self.scene_att_extraction(s[1]['text'], self.INT_EXT)[0],
                    'location': self.locsplit(s[1]['text'][0]),
                    'tod': self.scene_att_extraction(s[1]['text'], self.TOD)[0],
                    'transitions': self.scene_att_extraction(s[1]['text'], self.TRANSITIONS),
                    'action': self.extract_action(s[1]['text']),
                    'dialog': self.character_dialog(self.extract_dialogs(s[1]['text'])),

                }})

        return result
