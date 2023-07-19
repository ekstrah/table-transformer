import os


for subdir, dir, files in os.walk("."):
    for file in files:
        for a in ["train", "val", "test", "images"]:
            if subdir.startswith(f"./{a}"):
                with open(f"./{a}_filelist.txt", "a") as f:
                    f.writelines(os.path.join(subdir, file).replace("./", "")+"\n")