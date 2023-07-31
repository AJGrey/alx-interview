def validUTF8(data):
    # Function to check if a given number has the correct UTF-8 prefix
    def has_correct_prefix(byte):
        return (byte >> 6) in {2, 3, 4}

    # Number of bytes that the current UTF-8 character should have
    num_bytes = 0

    for byte in data:
        # Check if the current byte has the correct UTF-8 prefix
        if num_bytes == 0:
            if byte >> 7 == 0b0:
                # Single-byte character (ASCII character)
                num_bytes = 0
            elif byte >> 5 == 0b110:
                # Two-byte character
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                # Three-byte character
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                # Four-byte character
                num_bytes = 3
            else:
                # Invalid prefix
                return False
        else:
            if not has_correct_prefix(byte):
                # The bytes of multi-byte xter should have the prefix '10'
                return False
            num_bytes -= 1

    # If there are trailing bytes, it's an invalid UTF-8 encoding
    return num_bytes == 0
