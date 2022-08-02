import pandas as pd
import requests
import math
import threading
import time

class ImageDownloadThread(threading.Thread):
    def __init__(self, thread_id, name, img_list):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.img_list = img_list
        self.start_time = None
        self.end_time = None
        self.duration = None

    def run(self):
        try:
            self.start_time = time.time()
            print(f"Starting the save image process for thread {self.thread_id}")
            save_images(self.img_list)
        except Exception as e:
            print(f"Having problems persisting the images from the data onto file system for thread id: {self.thread_id} with error: {e}")
        finally:
            self.end_time = time.time()
            self.duration = self.end_time - self.start_time
            print(f"Successfully completed saving images for thread {self.thread_id}. Completing in {self.duration} seconds")

def save_images(img_list):
    error_img = list()
    assert len(img_list) > 0
    for img in img_list:
        img_url = img['picture_url']
        img_id = img['id']
        try:
            img_data = requests.get(img_url).content
            with open(f'/home/mgfos207/Desktop/Springboard/Module 26/assets/data/airbnb_images/{img_id}.jpg', 'wb') as handler:
                handler.write(img_data)
        except Exception as e:
            print(f"Issues with getting image id {img_id} with error: {e}")
            error_img.append(img_id)


def get_img_data(df):
    select_features = ['picture_url', 'id']
    subset_df = df[select_features]

    imgs_data = subset_df.to_dict('records')

    return imgs_data


def start_image_save(df):
    try:
        imgs_data = get_img_data(df)
        #split the data into chunks for the 10 threads
        data_length = len(imgs_data)
        chunks = math.ceil(data_length / 50)
        #store the chunks into different arrays perhaps a list of lists
        chunked_list = [imgs_data[i: i+chunks] for i in range(0, data_length, chunks)]
        #create different threads
        for idx, chunk in enumerate(chunked_list):
            img_thread = ImageDownloadThread(idx, f'img_thread-{idx}', chunk)
            img_thread.start()
    except Exception as e:
        print(f"Having problems persisting the images from the data onto file system: {e}")


def main():
    #read in the dataframe
    df = pd.read_csv("/home/mgfos207/Desktop/Springboard/Module 26/assets/data/orig/listings.csv")
    df.dropna(subset=['picture_url'], inplace=True)
    start_image_save(df)

    print("Finished")


if __name__ ==  "__main__":
    main()