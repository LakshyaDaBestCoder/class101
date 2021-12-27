import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            relativePath= os.path.relpath(local_path, file_from)
            dropboxPath= os.path.join(file_to, relativePath)

            with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropboxPath, mode=WriteMode("overwrite"))

def main():
    access_token = 'sl.A-nHh9M7jiTJaM23I9s38ACR7c-Ymph_GYdDxuaeUkyOWTzIe9TuZvJQOYofWuQQfP20VvAlUUWVk-Wo3t38AhOsxTJLPM1PfKKD89VEpQeMLU5NBr7FqA2mRQhV9flYpn9yUdc'
    transferData = TransferData(access_token)

    file_from = input("Insert the file_from")
    file_to = input("Insert the file_to")
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
