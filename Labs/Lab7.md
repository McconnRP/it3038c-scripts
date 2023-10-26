Here is how you can run a Python Script that I created, which uses the plugin called Pillow
First, we will need to create a Virtual ENV, you can call this whatever you want

    virtualenv ~/venv/pillow
    source ~/venv/scripts/bin/activate
    pip install pillow

This Scrips allows you to edit any photo you want!  Lets start with an image, it can be anything you choose.
Download the image and save it to your hard drive

In Python, run the following code

    from PIL import Image,ImageFilter
    myImage = Image.open('/full/path/to/image.jpg')
    myImage.load

This will load the image for you. Lets run some commands to get some specifications of the image.

    myImage.format
    myImage.size
    myImage.show()

Within this script showcase, I will provide 3 different instances you can use the Pillow plugin that you may find useful!

First:  Want to rotate an image on to its side?  Please run these commands against it to roll the image on its side.

     def roll(im, delta):
    """Roll an image sideways."""
    xsize, ysize = im.size
    
    delta = delta % xsize
    if delta == 0:
        return im

    part1 = im.crop((0, 0, delta, ysize))
    part2 = im.crop((delta, 0, xsize, ysize))
    im.paste(part1, (xsize - delta, 0, xsize, ysize))
    im.paste(part2, (0, 0, xsize - delta, ysize))

    return im

Second: Want to automatically enhance your image?  Pillow contains a handful of pre-defined enhancement filters that you can test out!

    from PIL import ImageFilter
    out = im.filter(ImageFilter.DETAIL)

Lastly: Do you have two similar images that you would like to merge?  Pillow allows you to do just that!  Please run these commands: 

    def merge(im1, im2):
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))

    return im

Dont forget to deactivate your VirtualEnv when you are done.

    deactivate 
