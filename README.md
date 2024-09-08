```markdown
# Video Mashup Project

This project automates the process of downloading YouTube videos, converting them to audio, cutting specific portions, merging them into one file, and sending the final output via email. It can be executed through the command line.

## Features

- Download N videos of a given singer from YouTube.
- Convert downloaded videos to audio files.
- Cut the first Y seconds from all downloaded audio files.
- Merge all the audio clips into one output file.
- Compress and send the final output via email using `yagmail`.

## Requirements

Make sure you have the following Python packages installed:

- `yt-dlp`
- `pydub`
- `ffmpeg` (Installed and configured in your system's PATH)
- `zipfile`
- `yagmail`

You can install the necessary Python libraries by running:

```bash
pip install yt-dlp pydub yagmail
```

You also need to download and configure `ffmpeg`. Follow instructions here to install it: [FFmpeg Installation Guide](https://ffmpeg.org/download.html).

## Email Setup with Yagmail

- Yagmail simplifies sending emails with Gmail accounts. Make sure you have a Gmail account, and that "Less secure apps" are enabled (or use an App Password if you have 2-factor authentication enabled).
- You'll also need to configure your Gmail account using `yagmail` before sending emails:
  
  ```bash
  pip install keyring
  yagmail.register('your_email@gmail.com', 'your_password')
  ```

This will store your credentials securely using the `keyring` library.

## Usage

To run the program, use the following command from the terminal:

```bash
python main.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName> <Email>
```

### Example

```bash
python main.py "Sharry Maan" 20 30 output.mp3 example@gmail.com
```

- `SingerName`: The name of the singer (e.g., Sharry Maan).
- `NumberOfVideos`: The number of videos to download.
- `AudioDuration`: The duration (in seconds) to cut from the start of each audio file.
- `OutputFileName`: The name of the final merged audio output file (e.g., `output.mp3`).
- `Email`: The email address to send the final output.

## Project Structure

```bash
├── main.py              # The main file that runs the entire pipeline
├── downloadder.py       # Script to download videos from YouTube
├── Converterr.py        # Script to convert videos to audio
├── cutter.py            # Script to cut audio to specified duration
├── Merger.py            # Script to merge audio files
├── zipsend.py           # Script to zip files and send email using yagmail
└── README.md            # Project documentation
```

## Steps in the Pipeline

1. **Download Videos**: The program downloads `N` videos from YouTube for the given singer name.
2. **Convert to Audio**: The downloaded videos are converted to audio files.
3. **Cut Audios**: Each audio file is trimmed to the first `Y` seconds.
4. **Merge Audios**: All the trimmed audios are merged into a single output file.
5. **Send Email**: The output file is zipped and sent to the provided email address using `yagmail`.

## Notes

- Ensure that the `ffmpeg` binary is properly installed and added to your system path to enable audio processing.
- The output audio files are merged into an `.mp3` file and sent as a zipped file via email using `yagmail`.
- Error handling and validation are implemented to ensure smooth execution.

## Troubleshooting

- **FFmpeg Issues**: If you encounter errors related to `ffmpeg`, make sure it's installed and available in your system's `PATH`.
- **Email Issues**: If you're facing issues with email, ensure `yagmail` is properly configured and that you're using the correct Gmail credentials.

## License

This project is licensed under the MIT License.
```