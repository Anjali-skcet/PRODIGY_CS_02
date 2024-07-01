from PIL import Image

def encrypt():

  path=input("\nEnter the path of the image:")
  value=int(input("\nEnter the shift value:"))

  image=Image.open(path)
  
  pix_val = list(image.getdata())

  new_pix=[]
  for i in pix_val:
        pix=[i[0]+value,i[1]+value,i[2]+value]
        if(pix[0]>255):
           pix[0]=pix[0]-256
        if(pix[1]>255):
           pix[1]=pix[1]-256
        if(pix[2]>255):
           pix[2]=pix[2]-256
        a=(pix[0],pix[1],pix[2])   
        new_pix.append(a)

  mimage = Image.new(image.mode, image.size)
  mimage.putdata(new_pix)

  save_path = "C:\\Users\\PS Anjali\\Downloads\\encrypted.png"
  mimage.save(save_path)
  mimage.show()


def decrypt():

  path=input("\nEnter path of the image:")
  value=int(input("\nEnter shift value:"))

  image=Image.open(path)

  pix_val = list(image.getdata())

  new_pix=[]
  for i in pix_val:
        pix=[i[0]-value,i[1]-value,i[2]-value]
        if(pix[0]<0):
           pix[0]=pix[0]+256
        if(pix[1]<0):
           pix[1]=pix[1]+256
        if(pix[2]<0):
           pix[2]=pix[2]+256
        a=(pix[0],pix[1],pix[2])   
        new_pix.append(a)

  mimage = Image.new(image.mode, image.size)
  mimage.putdata(new_pix)

  save_path = "C:\\Users\\PS Anjali\\Downloads\\decrypted.png"
  mimage.save(save_path)
  mimage.show()
 
operation=int(input("Enter the number for required ciphering method\n1 - Encryption\n2 - Decryption\n"))

if(operation==1):
  encrypt()
else:
  decrypt()