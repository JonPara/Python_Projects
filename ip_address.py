ipAddress = input("What is your IP address ? ")

segment = 1
segment_length = 0

for character in ipAddress:
    if character == ".":
        print("Segment {} contains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1
        
if character != '.':
    print("Segment {} contains {} characters".format(segment, segment_length))