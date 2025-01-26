# ConvertMKVFilesToMP4

Here’s a step-by-step guide to install FFmpeg and add it to your system’s PATH:

## Step 1: Download FFmpeg
Go to the official FFmpeg website: **https://ffmpeg.org/download.html.**
Under "Get packages & executable files", choose the appropriate link for your operating system:
For Windows, click on the Windows builds link (e.g., https://www.gyan.dev/ffmpeg/builds/).
Download the latest "Full" build in ZIP format.

## Step 2: Extract the FFmpeg ZIP
Locate the downloaded ZIP file (usually in your Downloads folder).
Right-click on the ZIP file and select Extract All.
Extract the contents to a folder (e.g., C:\ffmpeg).

## Step 3: Add FFmpeg to Your System PATH
Open the Start menu and type "Environment Variables", then select Edit the system environment variables.
In the System Properties window, click the Environment Variables button.
Under System Variables, find the Path variable and click Edit.
In the Edit Environment Variable window:
Click New.
Add the path to the FFmpeg bin folder (e.g., C:\ffmpeg\bin).
Click OK on all windows to save changes.

## Step 4: Verify the Installation
Open a Command Prompt:
Press Win + R, type cmd, and press Enter.
Type the following command:
Copy
Edit
ffmpeg -version
If installed correctly, you should see FFmpeg's version information.

## Step 5: Run the Python Script
Save the Python script from earlier as a .py file (e.g., convert_mkv_to_mp4.py).
Make sure you’ve installed Python on your system. If not, download it from https://www.python.org/downloads/.
Open Command Prompt, navigate to the directory containing the .py file, and run:
Copy
Edit
python convert_mkv_to_mp4.py
