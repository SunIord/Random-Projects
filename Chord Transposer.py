def transpose_line(line, steps):
  transposed_line = []
  for note in line.split():
    if note in chromatic_scale:
      note_index = chromatic_scale.index(note)
      transposed_index = (note_index + steps) % 12
      transposed_note = chromatic_scale[transposed_index]
      transposed_line.append(transposed_note)
    
    else:
      transposed_line.append(note)
  
  return " ".join(transposed_line)

chromatic_scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

#'steps' represents the number of semitone intervals to transpose the chords
steps = int(input())

notes = []
try:
  while True:
    line = input().strip().upper()
    notes.append(line)

except EOFError:
  print("Received Chords:")
  for note in notes:
    print(note)

transposed_notes = []
for line in notes:
  if " |" in line:
  #For cases where the lyrics follow each line, for example:
  #Em C7M G6 D9(11)/F# | Another head hangs lowly, child is slowly taken (Zombie by The Cranberries)
    chord_part, text_part = line.split(" |", 1)
    transposed_notes.append(transpose_line(chord_part, steps) + " |" + text_part)
  
  else:
    transposed_notes.append(transpose_line(line, steps))

print("\nTransposed Chords:")
for line in transposed_notes:
  print(line)
  
"""
Despite the example provided, the current code still does not fully support 
what I will refer to as "complex chords." 

While it handles "complex chords" correctly, they remain untransposed and 
appear unchanged in the output. These include:

- Chords with numbers (e.g., C7, D9(11)).
- Specifications of major or minor (e.g., C7M, Am).
- Chords with bass notes (e.g., D/F#, G/B).

I will be releasing the updated version soon.
"""
