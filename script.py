import subprocess
import os

# -------------------------------
# Paths
# -------------------------------
input_folder = r"C:\Users\zhiha\Downloads\vlog 2026"
output_folder = os.path.join(os.getcwd(), "ucla 2025")
os.makedirs(output_folder, exist_ok=True)

# -------------------------------
# Collect MOV files only
# -------------------------------
mov_files = []
for file in sorted(os.listdir(input_folder)):
    if file.endswith(".MOV"):
        mov_files.append(os.path.join(input_folder, file))

print(f"MOV files: {mov_files}")

# -------------------------------
# Merge MOV files with FFmpeg
# -------------------------------
if mov_files:
    file_list_path = os.path.join(output_folder, "file_list.txt")
    with open(file_list_path, "w") as f:
        for vf in mov_files:
            f.write(f"file '{vf}'\n")

    final_video_path = os.path.join(output_folder, "merged_video.mov")
    subprocess.run([
        "ffmpeg",
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", file_list_path,
        "-c", "copy",
        final_video_path
    ])

    print(f"Merged video saved to {final_video_path}")
else:
    print("No MOV files found to merge.")
