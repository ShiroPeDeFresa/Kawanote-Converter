from midiutil.MidiFile import MIDIFile

# def ms_a_qtn(val, bpm):
#     return (val * bpm / 60000)


def write_section(midi_file, hit_objects, start, end, bpm):
    midi_file.addTempo(0, start / bpm, bpm)
    
    contador = 0

    for hit_object in hit_objects:
        end = hit_objects[-1].position if end is None else end
        if hit_object.position <= end and hit_object.position >= start:
            
            time = hit_object.position / (60000 / bpm)
            duration= hit_object.length if hit_object.length == 0.05 else hit_object.length / (60000 / bpm)

            midi_file.addNote(track=0, channel=0, pitch=hit_object.column,time=time, duration=duration, volume=100)
            #print(contador)
        contador+=1

        
    return midi_file



