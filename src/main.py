import os, shutil

public_folder = "public"
static_folder = "static"

def clean_public():
    if os.path.exists(public_folder):
        for filename in os.listdir(public_folder):
            file_path = os.path.join(public_folder, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)    

def static_to_public_copy(working_folder, searching_folder):
    if os.path.exists(searching_folder):
        for filename in os.listdir(searching_folder):
            file_path = os.path.join(searching_folder, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                shutil.copy(file_path, working_folder)
            elif os.path.isdir(file_path):
                os.mkdir(f"{working_folder}/{filename}")
                new_working_folder = f"{working_folder}/{filename}"
                new_searching_folder = f"{searching_folder}/{filename}"
                static_to_public_copy(new_working_folder, new_searching_folder)


    


def main():
    clean_public()
    static_to_public_copy(public_folder, static_folder)


main()


