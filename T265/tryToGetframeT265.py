import numpy as np
import pyrealsense2 as rs
import cv2

def main():
    pipe = rs.pipeline()
    cfg = rs.config()
    cfg.enable_stream(rs.stream.fisheye, 1)
    cfg.enable_stream(rs.stream.fisheye, 2)

    pipe.start(cfg)

    try:
        while True:
            frames = pipe.wait_for_frames()

            lframe = frames.get_fisheye_frame(1)
            limage = np.asanyarray(lframe.get_data())
            rframe = frames.get_fisheye_frame(2)
            rimage = np.asanyarray(rframe.get_data())

            image = np.hstack((limage, rimage))

            height = image.shape[0]
            width = image.shape[1]

            image = cv2.resize(image, (int(width*0.5), int(height*0.5)))

            cv2.imshow('T265', image)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
    
    finally:
        pipe.stop()

if __name__ == "__main__":
    main()