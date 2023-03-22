from transfersh_client.app import send_to_transfersh, create_zip, remove_file

def uploadFile(filePath):
    sndFile = send_to_transfersh(filePath)
    return sndFile[:-1] 

