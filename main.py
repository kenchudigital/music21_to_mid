from music21 import *

# Create a Stream object
stream1 = stream.Stream()

# Add a key signature
stream1.append(key.KeySignature(1))

# Add a chord progression
chords = [chord.Chord(["C4", "E4", "G4"]), chord.Chord(["G4", "B4", "D5"]),
          chord.Chord(["C4", "E4", "G4"]), chord.Chord(["G4", "B4", "D5"]),
          chord.Chord(["C4", "E4", "G4"]), chord.Chord(["G4", "B4", "D5"]),
          chord.Chord(["C4", "E4", "G4"]), chord.Chord(["G4", "B4", "D5"])]

for c in chords:
    c.quarterLength = 2.0
    stream1.append(c)

# Set the tempo
stream1.insert(tempo.MetronomeMark(number=60))

# Show the score
stream1.show()

# Save the score as a MIDI file
mf = midi.translate.music21ObjectToMidiFile(stream1)
mf.open("ecommerce.mid", 'wb')
mf.write()
mf.close()