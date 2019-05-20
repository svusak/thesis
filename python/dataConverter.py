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
            print(data)
            hexData = ""



if __name__ == '__main__':
    generatePackets()
