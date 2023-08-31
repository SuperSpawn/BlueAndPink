def parse_text_string(text_string):
    # Initialize an empty array to store the objects
    object_array = []

    # Split the string by newline characters to get lines
    lines = text_string.split('\n')
    for line in lines:
        # Strip leading and trailing whitespace characters
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Split the line based on spaces
        parts = line.split(' ', 2)  # Maximum of 2 splits

        if len(parts) != 3:
            print(f"Skipping invalid line: {line}")
            continue

        # Extract the character, length, and text from the line
        character = parts[0]
        try:
            length = int(parts[1])
        except ValueError:
            print(f"Skipping invalid line: {line} (Invalid length)")
            continue
        text = parts[2]

        # Create an object and append to the array
        obj = {
            'character': character,
            'length': length,
            'text': text
        }
        object_array.append(obj)

    return object_array


__all__ = ['parse_text_string']
