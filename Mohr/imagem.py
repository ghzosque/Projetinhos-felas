from PIL import Image
import mohr

class Imagem:

    cu = mohr.Mohr()
    
    sigmaxx = cu.sigmaxx
    sigmayy = cu.sigmayy
    sigmaxy = cu.sigmaxy


    if (sigmaxx < 0) and (sigmayy < 0 ) and (sigmaxy < 0): #---
        im = Image.open('C:\\Users\\ghzos\\Desktop\\2k22 - CPITANIA\\Treinando\\Mohr\\DCL\\---.jpg')
        im.show()

    if (sigmaxx < 0) and (sigmayy < 0 ) and (sigmaxy > 0): #--+
        im = Image.open('C:\\Users\\ghzos\\Desktop\\2k22 - CPITANIA\\Treinando\\Mohr\\DCL\\--+.jpg')
        im.show()

    if (sigmaxx < 0) and (sigmayy > 0 ) and (sigmaxy < 0): #-+-
        im = Image.open('C:\\Users\\ghzos\\Desktop\\2k22 - CPITANIA\\Treinando\\Mohr\\DCL\\-+-.jpg')
        im.show()

    if (sigmaxx < 0) and (sigmayy > 0 ) and (sigmaxy > 0): #-++
        im = Image.open('C:\\Users\\ghzos\\Desktop\\2k22 - CPITANIA\\Treinando\\Mohr\\DCL\\-++.jpg')
        im.show()      

    if (sigmaxx > 0) and (sigmayy < 0 ) and (sigmaxy < 0): #+--
        im = Image.open('C:\\Users\\ghzos\\Desktop\\2k22 - CPITANIA\\Treinando\\Mohr\\DCL\\+--.jpg')
        im.show() 

    if (sigmaxx > 0) and (sigmayy < 0 ) and (sigmaxy > 0): #+-+
        im = Image.open('C:\\Users\\ghzos\\Desktop\\2k22 - CPITANIA\\Treinando\\Mohr\\DCL\\+-+.jpg')
        im.show() 

    if (sigmaxx > 0) and (sigmayy > 0 ) and (sigmaxy < 0): #++-
        im = Image.open('C:\\Users\\ghzos\\Desktop\\2k22 - CPITANIA\\Treinando\\Mohr\\DCL\\++-.jpg')
        im.show()

    if (sigmaxx > 0) and (sigmayy > 0 ) and (sigmaxy > 0): #+++
        im = Image.open('C:\\Users\\ghzos\\Desktop\\2k22 - CPITANIA\\Treinando\\Mohr\\DCL\\+++.jpg')
        im.show()  