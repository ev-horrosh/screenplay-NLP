phrases = ['INT.', 'EXT.', 'INT/EXT.', 'EXT/INT.']
text = ['INT. DEPT. OF HEALTH, OFFICE - MORNING',
        "CLOSE ON ARTHUR (30's), tears in his eyes from laughing so",
        "hard. He's trying to get it under control. His greasy, black",
        "TIME CUT Joker"
        "hair hanging down over his forehead. He's wearing an old,",
        "CUT TO: "
        'faded green cardigan sweater, a threadbare gray scarf, thin',
        'EXT.']


# def delete_phrases(text, phrases):
#     if len(phrases) == 1:  # if there's only one prase left in the list
#         result = [t for t in text if phrases[0] not in t]
#         return result
#     else:
#         for idx, phrase in enumerate(phrases):
#             result = [t for t in text if phrase not in t]
#  # chopping off the top of the list until we reach our final condition^^^
#             return delete_phrases(result, phrases[idx+1:])
# print(delete_phrases(text, phrases))
# for te in text:
#     print([t for t in phrases if t in te])

# -------------
TOD = ['AFTERNOON', 'CONTINUOUS', 'DAWN', 'DAY', 'DUSK',
           'EVENING', 'LATER', 'MORNING', 'NIGHT', 'NOON', 'SAME','SUNSET']
TRANSITIONS = ['BACK TO:', 'CUT TO:', 'DISSOLVE TO:', 'FADE IN:', 'CUT BACK TO:','CUT BACK TO:',
                'FADE OUT:', 'FADE TO:', 'JUMP CUT TO:', 'MATCH CUT TO:', 'TITLE:', 'QUICK CUTS:',
                'SMASH CUT TO:', 'TIME CUT:', 'WIPE TO:', 'CROSSFADE:', 'OVER BLACK:', 'CUT TO BLACK',
                'FADE TO:BLACK', 'FLASH CUT:', 'LAP DISSOLVE:', 'MATCH DISSOLVE TO:', 'SUPER:', 'IRIS OUT:']
SHOTS = ['AERIAL SHOT', 'ANGLE ON',  'CLOSE ON', 'CLOSER ANGLE', 'CONTINUOUS',
            'CONTRAZOOM', 'CRAWL',  'ESTABLISHING SHOT',
            'EXTREMELY LONG SHOT (XLS):', 'FAVOR ON','HEAR LAUGHTER.',
            'FLASHBACK:', 'FREEZE FRAME:', 'INSERT','DAYS LATER'
            'INTO FRAME:', 'INTO VIEW:', 'MOS', 'O.C. / O.S.',
            'POV', 'PULL BACK:', 'PULL FOCUS:', 'PUSH IN:',
            'REVERSE ANGLE',  'SPLIT SCREEN SHOT:', 'STOCK SHOT:',
            'TIGHT ON', 'TIME CUT', 'V.O.', 'ZOOM:']

# to leave 
# def scene_att_extraction(text, scene_attribute):
#     result = []
#     for line in text:
#         [result.append(t) for t in scene_attribute if t in line]
#     return result


# scenes_head={}
# for i,s in enumerate(text,start=1):
    
#     scenes_head.update({
#         'int_ext':[l for l in s.split()][0],
#                 'location':' '.join([l for l in s.split() if l not in self.TOD and l!='-'][1:-1]),
#                 'tod':[l for l in s.split() if l in self.TOD][0],
#                 'transitions':[t for t in self.scenes().split() if t in self.TRANSITIONS]
# }}) 

def locsplit(text):
    temp=' '.join([l for l in text.split() if l not in TOD][1:-1])
    def strip_dash(temp):
        if not temp.endswith('-'):
            return temp
        else:
            temp=temp.rstrip('- ')
            return strip_dash(temp)
    result=strip_dash(temp)
    return result
  

# print(' GOTHAM INT. SQUARE'.find('INT.'))

print(locsplit('EXT. GOTHAM SQUARE, MIDTOWN - AFTERNOON - DAYS LATER'))


print(locsplit("EXT. BACK ALLEY, OUTSIDE HA-HA'S - DAY"))

# print(locsplit(text[0]))
#  to delete