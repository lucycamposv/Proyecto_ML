import cv2

def bgr2rgb(img_BGR):
    '''
    Transforma la imagen bgr a rgb.

    Parameters
    ----------
    img_BGR : img

    Return
    ------
    img_RGB : img
    '''
    b,g,r = cv2.split(img_BGR)
    img_RGB = cv2.merge((r,g,b))
    return img_RGB

def eliminar_vello(imagen):
    '''
    Se aplica una máscara para eliminar el vello en la imagen. La función devuelve una `imagen` con las
    mismas dimensiones que la original.
    
    Parameters
    ----------
    imagen : img

    Output
    ------
    new_img : img

    '''
    #1. Convertir a escala de grises
    img_grayScale = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    # Kernel para el filtrado morfológico
    kernel = cv2.getStructuringElement(1,(17,17))
    # Filtrado BlackHat para encontrar los contornos del cabello
    blackhat = cv2.morphologyEx(img_grayScale, cv2.MORPH_BLACKHAT, kernel)
    # Intensificar los contornos del cabello en preparación para el algoritmo de pintura
    ret,thresh2 = cv2.threshold(blackhat,12,255,cv2.THRESH_BINARY)
    # Pintar la imagen original dependiendo de la máscara
    new_img = cv2.inpaint(imagen,thresh2,1,cv2.INPAINT_TELEA)
    return new_img

def mask_fondo(imagen):
    '''
    Función para eliminar el fondo de la imagen.

    Parameters
    ----------
    imagen : img

    Output
    ------
    res : img
    '''
    gray_example = cv2.cvtColor(eliminar_vello(imagen), cv2.COLOR_BGR2GRAY)
    thresh, im_bw = cv2.threshold(gray_example, 120, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    mask_inv = cv2.bitwise_not(im_bw) 
    res = cv2.bitwise_and(imagen,imagen,mask = mask_inv)
    return res