from detect import MODEL
from PIL import Image
import numpy as np

# 将RGB图和DEPTH图进行堆叠，形状为[w, h, 6]
rgb = np.array(Image.open('RGB.jpg'))
rgb_sticker = np.array(Image.open('RGB-sticker.jpg'))
depth = np.array(Image.open('DEPTH.jpg'))
assert rgb.shape == depth.shape == rgb_sticker.shape, "图像尺寸必须匹配"
rgb_depth = np.dstack((rgb, depth))
rgb_sticker_depth = np.dstack((rgb_sticker, depth))
np.save('RGB_DEPTH.npy', rgb_depth)
np.save('RGB_DEPTH_sticker.npy', rgb_sticker_depth)

result1 = MODEL(
    weights="best.pt",  # model path or triton URL
    source="RGB_DEPTH.npy",  # file/dir/URL/glob/screen/0(webcam)
    imgsz=(640, 640),  # inference size (height, width)
    conf_thres=0.25,  # confidence threshold
    iou_thres=0.45,  # NMS IOU threshold
    save=True,  # save img results
    save_txt=True,  # save results to *.txt
    augment=False,  # augmented inference
    project="runs",  # save results to project/name
    name="nosticker",  # save results to project/name
)

result2 = MODEL(
    weights="best.pt",  # model path or triton URL
    source="RGB_DEPTH_sticker.npy",  # file/dir/URL/glob/screen/0(webcam)
    imgsz=(640, 640),  # inference size (height, width)
    conf_thres=0.25,  # confidence threshold
    iou_thres=0.45,  # NMS IOU threshold
    save=True,  # save img results
    save_txt=True,  # save results to *.txt
    augment=False,  # augmented inference
    project="runs",  # save results to project/name
    name="sticker",  # save results to project/name
)