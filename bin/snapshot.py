#!/usr/bin/env python

# http://opencv.willowgarage.com/wiki/Mac_OS_X_OpenCV_Port
# http://astrobeano.blogspot.com/2012/02/webcam-capture-with-python-on-mac-os-x.html

import sys
import time
import os.path
import cv2

def capture(camera):

    vidcap = cv2.VideoCapture()
    vidcap.open(camera)

    retval, image = vidcap.retrieve()
    vidcap.release()
    
    now = int(time.time())
    fname = "snapshot-%s.jpg" % now

    cv2.imwrite(fname, image)
    return os.path.realpath(fname)

if __name__ == '__main__':

    import optparse

    parser = optparse.OptionParser()
    parser.add_option("-c", "--camera", dest="camera", help="...", default=0, type="int")
    parser.add_option("-s", "--save-as", dest="saveas", help="...", default=None)

    (opts, args) = parser.parse_args()
    
    path = capture(opts.camera)

    if opts.saveas:
      
        saveas = os.path.realpath(opts.saveas)
        os.rename(path, saveas)
        path = saveas

    print "your new snapshot: %s" % path
    sys.exit()
