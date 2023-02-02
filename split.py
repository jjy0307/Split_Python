from PIL import Image

def split(input, output):
    img = Image.open(input)
    (img_w, img_h) = img.size

    grid_w = 300
    grid_h = 300

    range_w = int(img_w/grid_w)
    range_h = int(img_h/grid_h)

    i = 0
 
    for w in range(range_w):
        for h in range(range_h):
            bbox = (w*grid_w, h*grid_h, (w+1)*grid_w, (h+1)*grid_h)
            split_img = img.crop(bbox)            
 
            filename = "{}.png".format(i)
            savename = output + filename
            split_img.save(savename)

            i += 1
 

if __name__ == '__main__':
    split(input image, output path)
