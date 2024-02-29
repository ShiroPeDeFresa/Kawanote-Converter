from midiutil.MidiFile import MIDIFile
import Interface, hit_object, midi_writer, read_file
import read_file
import midi_writer
import os 
import sys
from PySide6.QtWidgets import QApplication

osu_file = None
desktop_path = None

def handle_selection(file, destination):
    try:

        osu_file= file
        converts_folder = destination

        headers = read_file.getHeaders(osu_file)
        timing_points = read_file.getTimingPoints(osu_file)
        hit_objects = read_file.getHitObjects(osu_file)

        midi_file = MIDIFile(numTracks=1,
                            removeDuplicates=False,
                            deinterleave=True,
                            adjust_origin=False,
                            file_format=1,
                            ticks_per_quarternote=960,
                            eventtime_is_ticks=False)


        midi_file.addTrackName(track=0, time=0, trackName=headers.get('version'))


        for index in range(len(timing_points)):
            tp_item = timing_points[index].split(',')

            section_start = int(tp_item[0])
            if index == len(timing_points) -1:
                section_end = None
            else:
                section_end = int(timing_points[index+1].split(',')[0]) 

            bpm = 60000 // float(tp_item[1])
            print(index)

            midi_file = midi_writer.write_section(midi_file, hit_objects, section_start, section_end, bpm)
        
        
        output_file_path = os.path.join(converts_folder, f"{headers.get('version')}.mid")

        with open(output_file_path, 'wb') as output:
            midi_file.writeFile(output)
    
    except Exception as e:
        with open('error.log', 'w', encoding='utf-8') as elog:
            elog.write(str(e))


app = QApplication(sys.argv)
window = Interface.FileTransferApp()

window.selection_completed.connect(handle_selection)  # Conexión a la señal

window.show()

sys.exit(app.exec_())
