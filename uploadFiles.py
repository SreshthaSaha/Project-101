import dropbox

class MoveData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
    
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = "XtpS0CoAGZoAAAAAAAAAATDzdrCVcorTE6OlhVKrtZDYM8NYzK5C0y6_kpjDHMmc"
    moveData = MoveData(access_token)

    file_from = input("Enter the file name you want to upload: ")
    file_to = input("Enter the full path to dropbox: ")
    moveData.upload_file(file_from, file_to)

main()
