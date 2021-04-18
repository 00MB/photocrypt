from PIL import Image, ImageDraw

def ascifii():
    # chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"[::-1]
    # chars = "%B@$" 
    # chars = " -oW#"
    chars ="`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    img = Image.open("pure.png")
    scale = 0.2
    width , height = img.size 
    img = img.resize((int(scale*width), int(scale*height*0.55555)) , Image.NEAREST)
    width , height = img.size 
    pix = img.load()

    outputImg = Image.new('RGB',(10*width, 18*height), color =(0,0,0))
    draw = ImageDraw.Draw(outputImg)
    ascii_string = ""

    for i in range(height):    
        for j in range(width):
            r, g, b = pix[j,i]
            avg = int((r/3 + g/3 + b/3))
            pix[j, i] = (avg , avg , avg)
            charToAdd = chars[int((float(avg)/255)*len(chars))]
            draw.text((j*10 , i*18), charToAdd  , fill =(255,255,255))
            ascii_string += charToAdd
    #outputImg.save("tmp/output.png")
    return ascii_string