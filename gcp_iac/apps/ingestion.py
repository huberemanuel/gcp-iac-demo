import tempfile
import shutil
import os
from threading import Thread
from queue import Queue
import subprocess

from google.cloud import storage
from tensorflow.keras.datasets.fashion_mnist import load_data
from PIL import Image
from tqdm import tqdm

from gcp_iac.resources import gcp_iac_bucket_name, gcp_iac_project_id


def ingest_initial_data(project_id : str, bucket_name : str):

    (x_train, y_train), (x_test, y_test) = load_data()
    dataset = {
        "train": {
            "x": x_train,
            "y": y_train
        },
        "test": {
            "x": x_test,
            "y": y_test
        }
    }
    classes = {
        0: "t-shirt",
        1: "trouser",
        2: "pullover",
        3: "dress",
        4: "coat",
        5: "sandal",
        6: "shirt",
        7: "sneaker",
        8: "bag",
        9: "ankle-boot"
    }

    temp_dir = tempfile.mkdtemp()
    temp_file_names = []

    for set_name, data in dataset.items():
        for i, (item, label) in tqdm(enumerate(zip(data["x"], data["y"]))):
            label_name = classes[label]

            im = Image.fromarray(item)
            file_path = f"datasets/fashion-mnist/{set_name}/{label_name}"
            temp_path = os.path.join(temp_dir, file_path)
            if not os.path.exists(temp_path):
                os.makedirs(temp_path)
            file_name = os.path.join(file_path, f"{i}.jpg")
            temp_file_name = os.path.join(temp_dir, file_name)
            im.save(temp_file_name)

            temp_file_names.append((temp_file_name, file_name))

    try:

        dst = f"gs://{gcp_iac_bucket_name}/"
        process_str = f"gsutil -m rsync -r {temp_dir} {dst}"
        subprocess.run(process_str, shell=True)

    finally:
        shutil.rmtree(temp_dir)

    print("Succesfully ingested Fashion MNist dataset")

def upload_file(upload_queue : Queue, upload_bar):
    while True:
        storage_client, bucket_name, ori_file_name, dest_file_name = upload_queue.get()
        bucket = storage_client.get_bucket(bucket_name)
        if not storage.Blob(bucket=bucket, name=dest_file_name).exists(storage_client):
            blob = bucket.blob(dest_file_name)
            blob.upload_from_filename(ori_file_name)
        upload_bar.update()
        upload_queue.task_done()

if __name__ == "__main__":
    ingest_initial_data(gcp_iac_project_id, gcp_iac_bucket_name)