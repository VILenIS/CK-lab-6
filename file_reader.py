print('HEllo!\nPlease write a file path\n')
path = str(input())
def reader(path):
    try:
        with open(path, mode='r') as file:
            print('Cодержимое файла :')
            filer = file.readlines()
            for i in range(len(filer)):
                print(filer[i][:len(filer[i])-2:1])
            file.close()

    except:
        print("ERROR")

reader(path)

