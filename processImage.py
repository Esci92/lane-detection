from laneDetectionMethods import *

#Test on a single image
test_images = [read_image('test_images/b.JPG')]
print(test_images[0].shape)
draw_lane_lines(test_images[0])
plt.savefig('output/result_Image.png', dpi=600, format='png')
plt.show()
