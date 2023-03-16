import sys
import re
from pathlib import Path
from gtts import gTTS
from pydub import AudioSegment
import re

def parse_fountain(fountain_str):
    lines = fountain_str.split('\n')
    elements = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.startswith('>'):
            element_type = 'Action'
            text = line[1:].strip()
        elif line.startswith('*'):
            element_type = 'Transition'
            text = line[1:].strip()
        else:
            character_match = re.match(r'^([A-Z]+(?:[ ][A-Z]+)*)$', line)
            if character_match:
                element_type = 'Character'
                text = character_match.group(1)
            else:
                element_type = 'Dialogue'
                text = line

        elements.append({'type': element_type, 'text': text})

    return elements

def parse_fountain_file(file_path):
    with open(file_path, "r") as f:
        fountain_data = parse_fountain(f.read())
    return fountain_data

def generate_character_voices(fountain_data, output_dir):
    voices = {}
    for element in fountain_data.elements:
        if element['type'] == 'Character':
            character = element['text'].strip()
            if character not in voices:
                voices[character] = []

    for character in voices:
        lang = "en"
        tts = gTTS(character, lang=lang)
        file_path = output_dir / f"{character}.mp3"
        tts.save(str(file_path))
        voices[character] = AudioSegment.from_mp3(file_path)

    return voices

def create_audio_output(fountain_data, voices, output_file):
    output_audio = AudioSegment.empty()

    for element in fountain_data.elements:
        if element['type'] == 'Dialogue':
            character = element['character'].strip()
            voice = voices.get(character)
            if voice:
                tts = gTTS(element['text'].strip())
                tts.save("temp.mp3")
                audio_segment = AudioSegment.from_mp3("temp.mp3")
                output_audio += voice[:1000] + audio_segment

    output_audio.export(output_file, format="mp3")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fountain_to_audio.py <fountain_file> <output_audio_file>")
        sys.exit(1)

    fountain_file = sys.argv[1]
    output_audio_file = sys.argv[2]
    output_dir = Path("voices")

    output_dir.mkdir(parents=True, exist_ok=True)

    fountain_data = parse_fountain_file(fountain_file)
    voices = generate_character_voices(fountain_data, output_dir)
    create_audio_output(fountain_data, voices, output_audio_file)

def parse_fountain(fountain_str):
    lines = fountain_str.split('\n')
    elements = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.startswith('>'):
            element_type = 'Action'
            text = line[1:].strip()
        elif line.startswith('*'):
            element_type = 'Transition'
            text = line[1:].strip()
        else:
            character_match = re.match(r'^([A-Z]+(?:[ ][A-Z]+)*)$', line)
            if character_match:
                element_type = 'Character'
                text = character_match.group(1)
            else:
                element_type = 'Dialogue'
                text = line

        elements.append({'type': element_type, 'text': text})

    return elements
