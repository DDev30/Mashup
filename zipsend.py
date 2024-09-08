import shutil
import yagmail
import argparse

def zip_and_email_folder(folder, recipient):
    zip_path = shutil.make_archive(folder, 'zip', folder)
    yagmail.SMTP('dv30arya@gmail.com', 'fdib wech jves elmv').send(
        to=recipient,
        subject="Zipped Folder: Merged Audio Files",
        contents=f"Attached is the zipped folder {folder}.",
        attachments=zip_path
    )
    print(f"Email sent to {recipient} with {zip_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("folder")
    parser.add_argument("recipient")

    args = parser.parse_args()
    zip_and_email_folder(args.folder, args.recipient)