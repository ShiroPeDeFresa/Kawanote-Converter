from midiutil.MidiFile import MIDIFile
import hit_object

def getHeaders(file_path):
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
        position = int(items[2])
        note_type = int(items[5].split(':', 1)[0]) # <- 0 si es rice, >1 si es LN

        length = (0.05 if note_type == 0 else note_type - position)  # <- Esta línea hace ese split porque quiere coger solo el primer parametro de la seccion
                                                                                                    # ultima de la linea con formato "32785:0:0:0:0:"
        hit_object_list.append(hit_object.HitObject(column, position, length))
  
        line = beatmap.readline()

    beatmap.close()
    return hit_object_list


if __name__ == '__main__':
    osu_file = input("Ruta al fichero: ")

    headers = getHeaders(osu_file)
    timing_points = getTimingPoints(osu_file)
    hit_objects = getHitObjects(osu_file)

    print('miau')