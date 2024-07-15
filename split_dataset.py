import os
import shutil
import random


def check_missing_txt_files(txt_folder, img_folder):
    txt_files = [os.path.splitext(f)[0] for f in os.listdir(txt_folder) if f.endswith('.txt')]
    img_files = [os.path.splitext(f)[0] for f in os.listdir(img_folder) if f.endswith('.jpg')]
    missing_txt_files_for_imgs = [f + ".jpg" for f in img_files if f not in txt_files]
    return missing_txt_files_for_imgs


def distribute_dataset(img_folder, txt_folder, yaml_paths):
    img_files = sorted([f for f in os.listdir(img_folder) if f.endswith('.jpg')])
    txt_files = sorted([f for f in os.listdir(txt_folder) if f.endswith('.txt')])
    combined = list(zip(img_files, txt_files))
    random.shuffle(combined)
    img_files[:], txt_files[:] = zip(*combined)
    total_files = len(img_files)
    train_size = int(0.8 * total_files)
    val_size = int(0.1 * total_files)
    train_img_files = img_files[:train_size]
    train_txt_files = txt_files[:train_size]
    val_img_files = img_files[train_size:train_size + val_size]
    val_txt_files = txt_files[train_size:train_size + val_size]
    test_img_files = img_files[train_size + val_size:]
    test_txt_files = txt_files[train_size + val_size:]
    for img, txt in zip(train_img_files, train_txt_files):
        shutil.move(os.path.join(img_folder, img), os.path.join(yaml_paths['train_img'], img))
        shutil.move(os.path.join(txt_folder, txt), os.path.join(yaml_paths['train_txt'], txt))
    for img, txt in zip(val_img_files, val_txt_files):
        shutil.move(os.path.join(img_folder, img), os.path.join(yaml_paths['val_img'], img))
        shutil.move(os.path.join(txt_folder, txt), os.path.join(yaml_paths['val_txt'], txt))
    for img, txt in zip(test_img_files, test_txt_files):
        shutil.move(os.path.join(img_folder, img), os.path.join(yaml_paths['test_img'], img))
        shutil.move(os.path.join(txt_folder, txt), os.path.join(yaml_paths['test_txt'], txt))
    return len(train_img_files), len(val_img_files), len(test_img_files)


# Paths
img_folder_path = ""
txt_folder_path = ""
yaml_paths = {
    'train_img': "",
    'train_txt': "",
    'val_img': "",
    'val_txt': "",
    'test_img': "",
    'test_txt': ""

}

# Check for missing txt files
missing_files_list = check_missing_txt_files(txt_folder_path, img_folder_path)
if missing_files_list:
    print(f"Missing txt files for the following images: {missing_files_list}")
else:
    train_count, val_count, test_count = distribute_dataset(img_folder_path, txt_folder_path, yaml_paths)
    print(f"Files distributed as - Train: {train_count}, Validation: {val_count}, Test: {test_count}")
