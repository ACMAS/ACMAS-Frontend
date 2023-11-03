import hashlib
import os
import vt


def hash_file(file_path):
   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(file_path,'rb') as file:
       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

def scan_file(file_path):
    VT_API_KEY = os.environ.get("VT_API_KEY", default="")
    client = vt.Client(apikey=VT_API_KEY, agent='ACMAS')
    # file_hash = hash_file(file_path)
    file = client.get_object(file_hash)
    if file.last_analysis_stats['malicious'] > 0:
        return 'malicious'
    elif file.last_analysis_stats['suspicious'] > 0:
        return 'suspicious'
    elif file.last_analysis_stats['harmless'] > 0:
    with open(file_path, 'rb') as f:
        # Scan the file and block until it is scanned
        analysis = client.scan_file(f, wait_for_completion=True)

    # try:
    #     analysis = client.scan_file(file_path, wait_for_completion=True)
    #     return analysis
    # except vt.APIError as e:
    #     print(e)
    #     return None
