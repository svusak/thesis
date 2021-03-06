from subprocess import Popen, PIPE


def hexStringToByteArray(hexString):
    return bytearray.fromhex(hexString)


def byteArrayToHexString(byteArray):
    return byteArray.hex()


def run(command):
    process = Popen(command, stdout=PIPE, shell=True)
    while True:
        line = process.stdout.readline().decode()
        if not line:
            break
        yield line


def generatePackets():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    s.connect((host, port))

    f = open("file.txt", "w+")
    packages = []

    hexData = ""

    for line in run("kissutil -v"):

        if line.startswith(" "):
            hexData += line[8:55].replace(' ', '');

        if line.startswith("[0]"):
            data = hexData[4:-2]
            packages.append(data)
            f.write(data + '\n')
            s.send(data)
            print(data)
            hexData = ""



if __name__ == '__main__':
    generatePackets()
