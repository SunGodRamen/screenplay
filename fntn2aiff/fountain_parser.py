import os
import re
from gtts import gTTS
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

def convert_line_to_mp3(line, voice_id, engine):
    with tempfile.NamedTemporaryFile(delete=False) as fp:
        temp_filename = fp.name

    engine.setProperty('voice', voice_id)
    engine.save_to_file(line, temp_filename)
    engine.runAndWait()

    return temp_filename

def generate_audio_files(characters, file_path):
    print(f"Generating audio files for characters: {characters}")

    with open(file_path, 'r') as file:
        content = file.readlines()

    audio_files = []

    for index, line in enumerate(content):
        is_dialogue = False
        character = ""

        # Check if the line is a character name
        if line.strip() in characters:
            character = line.strip()
            is_dialogue = True

        # Check if the line is dialogue
        elif index > 0 and content[index - 1].strip() in characters:
            character = content[index - 1].strip()
            is_dialogue = True

        if is_dialogue:
            tts = gTTS(text=line.strip(), lang='en')
            output_file = f"audio/{character}-{index}.mp3"
            tts.save(output_file)
            audio_files.append(output_file)

    print(f"Generated audio files: {audio_files}")
    return audio_files

def concatenate_audio(audio_files, output_file):
    print(f"Concatenating audio files: {audio_files}")

    concatenated_audio = AudioSegment.empty()

    for audio_file in audio_files:
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

