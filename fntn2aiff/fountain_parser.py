import os
import re
from gtts import gTTS
from gtts import lang
gTTS.GOOGLE_TTS_URL = 'https://translate.google.com/translate_tts'
lang.tld = 'com'
from pydub import AudioSegment

def parse_fountain_file(file_path):
    print(f"Processing Fountain file: {file_path}")
    with open(file_path, 'r') as file:
        content = file.readlines()

    characters = set()

    for i, line in enumerate(content[:-1]):
        next_line = content[i + 1]

        uppercase_condition = re.match(r'^[A-Z\s\-\.]+$', line.strip())
        no_lowercase_digits_condition = not re.search(r'[a-z0-9]', line.strip())
        next_line_not_empty_condition = re.match(r'^\S+.*$', next_line.strip())

        if bool(uppercase_condition) and bool(no_lowercase_digits_condition) and bool(next_line_not_empty_condition):
            characters.add(line.strip().rstrip('*'))

        else:
            dialogue_character_match = re.match(r'^([A-Z]+)\s*$', line.strip())
            if dialogue_character_match:
                characters.add(dialogue_character_match.group(1))

    print(f"Characters found: {characters}")
    return list(characters)

def generate_audio_files(characters, file_path, output_dir="audio"):
    print(f"Generating audio files for characters: {characters}")

    voices_list = [
        {"lang": "en", "accent": "com"},
        {"lang": "en", "accent": "uk"},
        {"lang": "en", "accent": "au"},
        {"lang": "en", "accent": "ca"},
        {"lang": "en", "accent": "za"},
    ]  # List of 5 different voices
    character_voices = {character: voice for character, voice in zip(characters, voices_list)}
    narrator_voice = {"lang": "en", "accent": "uk"}  # Set the narrator's voice for stage directions

    audio_files = []
    line_number = 1
    stage_direction_mode = False

    with open(file_path, 'r') as file:
        for line in file.readlines():
            line = line.strip()

            if not line:  # Skip blank lines
                stage_direction_mode = False
                continue

            if line.startswith('>') and line.endswith('<'):
                line = line[1:-1].strip()
                character = None
                voice = narrator_voice
            else:
                character = next((c for c in characters if line.startswith(c)), None)
                if character:
                    line = line[len(character):].strip()
                    voice = character_voices.get(character, narrator_voice)
                    stage_direction_mode = False
                else:
                    if not stage_direction_mode:
                        stage_direction_mode = True
                        character = None
                        voice = narrator_voice
                    else:
                        line_number += 1
                        continue

            # Skip line if it only contains whitespace characters
            if not line.strip():
                line_number += 1
                continue

            output_file = f"{output_dir}/{character or 'NARRATOR'}-{line_number}.mp3"
            audio_files.append(output_file)
            tts = gTTS(text=line, lang=voice["lang"], tld=voice["accent"])
            tts.save(output_file)

            line_number += 1

    return audio_files

def concatenate_audio(audio_files_dict, output_file):
    print(f"Concatenating audio files: {audio_files_dict}")

    concatenated_audio = AudioSegment.empty()

    for character, audio_file in audio_files_dict.items():
        segment = AudioSegment.from_file(audio_file, format="mp3")  # Change format to "mp3"
        concatenated_audio += segment

    concatenated_audio.export(output_file, format="mp3")

def main():
    input_dir = os.environ.get('INPUT_DIR', 'input')
    output_dir = os.environ.get('OUTPUT_DIR', 'output')

    file_path = os.path.join(input_dir, 'sample_fountain_script.fountain')
    output_file = os.path.join(output_dir, 'output.mp3')

    # Create the audio directory if it doesn't exist
    os.makedirs('audio', exist_ok=True)

    print("Starting Fountain file processing...")
    characters = parse_fountain_file(file_path)
    audio_files = generate_audio_files(characters, file_path)
    concatenate_audio(audio_files, output_file)
    print("Fountain file processing complete.")

if __name__ == "__main__":
    main()

