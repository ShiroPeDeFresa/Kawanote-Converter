from midiutil.MidiFile import MIDIFile
import hit_object

OFFSET_TO_FIX = 0
KEYMODE = ''

def getHeaders(file_path):
    global KEYMODE
    headers = {}
    beatmap = open(file_path, "r", encoding='utf-8')

    line = beatmap.readline()

    while "Title:" not in line:
        line = beatmap.readline()
        headers['title'] = line[6:-1]

    while "Version:" not in line:
        line = beatmap.readline()
        headers['version'] = line[8:-1]

    while "CircleSize:" not in line:
        line = beatmap.readline()
        headers['keymode'] = line[11:-1]
        KEYMODE = line[11:-1]
        
    beatmap.close()
    return headers

def getTimingPoints(file_path):
    tp_list = []
    beatmap = open(file_path, "r", encoding='utf-8')

    line = beatmap.readline()

    while "[TimingPoints]" not in line:
        line = beatmap.readline()

    line = beatmap.readline()
    while "," in line:
        items = line.split(',')
        point_type = 'timing_point' if int(items[6]) == 1 else 'inherited_point'

        if point_type == "timing_point":
            tp_list.append(line)
        
        line = beatmap.readline()

    if int(tp_list[0].split(',')[0]) < 0:
        fix_negative_offset(tp_list)

    beatmap.close()
    return tp_list

def getHitObjects(file_path):
    hit_object_list = []
    beatmap = open(file_path, "r", encoding='utf-8')

    line = beatmap.readline()

    while "[HitObjects]" not in line:
        line = beatmap.readline()

    line = beatmap.readline()
    while "," in line: 
        items = line.split(',') 
        
        column = int(items[0])
        position = int(items[2]) if OFFSET_TO_FIX == 0 else int(items[2]) + OFFSET_TO_FIX
        note_type = int(items[5].split(':', 1)[0]) # <- 0 si es rice, >1 si es LN

        length = (0.05 if note_type == 0 else note_type - position)  # <- Esta línea hace ese split porque quiere coger solo el primer parametro de la seccion
                                                                                                    # ultima de la linea con formato "32785:0:0:0:0:"
        hit_object_list.append(hit_object.HitObject(column, position, length))
  
        line = beatmap.readline()

    beatmap.close()
    return hit_object_list

#Funcion que arregla los offset negativos
def fix_negative_offset(tp_list):
    global OFFSET_TO_FIX

    OFFSET_TO_FIX = int(tp_list[0].split(',')[0]) * -1

    for i in range(len(tp_list)):
        items = tp_list[i].split(',')
        items[0] = str(int(items[0]) + OFFSET_TO_FIX)
        tp_list[i] = ','.join(items)



if __name__ == '__main__':
    osu_file = input("Ruta al fichero: ")

    headers = getHeaders(osu_file)
    timing_points = getTimingPoints(osu_file)
    hit_objects = getHitObjects(osu_file)

    print('miau')