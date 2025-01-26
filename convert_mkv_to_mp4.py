import os
import subprocess

# Define the directory containing the videos
directory = r"C:\Users\chrisjallaine\Downloads\Movies\Action"

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".mkv"):
        
        # Build full file paths
        original_path = os.path.join(directory, filename)
        new_name = f"{os.path.splitext(filename)[0]} - MP4 Converted.mkv"
        renamed_path = os.path.join(directory, new_name)
        converted_path = os.path.join(directory, f"{os.path.splitext(filename)[0]}.mp4")
        
        try:
            # Convert MKV to MP4 using FFmpeg
            subprocess.run(
                ["ffmpeg", "-i", original_path, "-c:v", "copy", "-c:a", "copy", converted_path],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            # Rename the original file
            os.rename(original_path, renamed_path)
            print(f"Converted and renamed: {filename}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {filename}: {e}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("All conversions completed.")
