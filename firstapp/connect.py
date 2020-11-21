import os

def connect(file_path, mediadir, file_name):
    print('*'*50)
    print('connect')
    print('*'*50)

    print("file_path: ", file_path)
    print("mediadir: ", mediadir)
    print("file_name: ", file_name)
    
    detect_connect(file_path, mediadir, file_name)

def detect_connect(file_path, mediadir, file_name):
    print('*'*30)
    print('detect_connect')   
    print('*'*30)

    print("in detect.py")
    print(file_path)
    print(mediadir)
    print(file_name)
    
    current_path = os.getcwd()
    print("current path: ", current_path)
    input_path = os.path.relpath(
        current_path + '/media/' + str(file_name), current_path)
    print("relative input path: ", input_path)

    output_path = os.path.relpath(
        current_path + '/results/' + str(file_name), current_path)
    print("relative output path: ", output_path)

    arg = "python demo_video.py --input " + input_path + " --output " + output_path
    os.system("cd ..")
    os.system(arg)
    os.system("cd firstapp")
    return