import sys
import re
import pyttsx3

def parse_fountain_file(file_path):
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

    return list(characters)

def convert_to_mp3(input_file, output_file, characters):
    # Initialize TTS engine
    engine = pyttsx3.init()

    # Load Fountain file content
    with open(input_file, 'r') as file:
        content = file.read()

    # Extract dialogues
    dialogues = re.findall(r'^[A-Z\s\-\.]+$\n^(\S+.*$)', content, re.MULTILINE)

    # Convert dialogues to speech and save as MP3
    for dialogue in dialogues:
        engine.save_to_file(dialogue, output_file)
    engine.runAndWait()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python fountain_parser.py <fountain_file_path> <output_mp3_path>')
        sys.exit(1)

    fountain_file_path = sys.argv[1]
    output_mp3_path = sys.argv[2]
    characters = parse_fountain_file(fountain_file_path)
    convert_to_mp3(fountain_file_path, output_mp3_path, characters)
