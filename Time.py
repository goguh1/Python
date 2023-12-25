# Project 1 and 2 delt with frames, let's turn some
# Into timecode.
# Write a script that takes a frame and turns it into
# Working timecode at 24 fps.
# Use frame examples: 35, 1569, 14000

fps = 24
frames = [35, 1569, 14000]

for frame in frames:
    total_seconds = frame / fps
    hours = int(total_seconds // 3600)
    total_seconds %= 3600
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    frames = frame % fps

    timecode = f"{hours:02d}:{minutes:02d}:{seconds:02d}:{frames:02d}"
    print(f"Frame {frame} timecode is {timecode} at 24 fps.")
