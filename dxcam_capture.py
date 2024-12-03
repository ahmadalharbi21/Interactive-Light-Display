import dxcam
from PIL import Image
import numpy as np
from collections import deque

color_queue = deque(maxlen=3)

def get_average_color(image, resize):
    image = image.resize(resize, resample=0)
    colors_array = np.array(image.getdata())
    average_color = tuple(int(x) for x in np.mean(colors_array, axis=0))
    color_queue.append(average_color)
    # Calculate the moving average color
    moving_average_color = tuple(int(np.mean(x)) for x in zip(*color_queue))
    return moving_average_color

def run_dxcam_capture(args):
    while True:
        try:
            camera = dxcam.create()
            camera.start(target_fps=args.fps, video_mode=True)
            while True:
                dxc_image = camera.get_latest_frame()
                image = Image.fromarray(dxc_image)
                average_color = get_average_color(image, args.resize)
                color_queue.append(average_color)
        except ValueError as e:
            if "could not broadcast input array from shape" in str(e):
                print(f"Resolution changed. Restarting camera with new resolution.")
                camera.stop()  # Stop the current camera
                continue  # Restart the outer loop to create a new camera object
            else:
                raise e