import numpy as np
from random import randint

#variant 1
def add_gaussian_noise(image_in, noise_sigma = 15):
    noise_sigma = randint(1,noise_sigma)
    temp_image = np.float64(np.copy(image_in))

    h = temp_image.shape[0]
    w = temp_image.shape[1]
    noise = np.random.randn(h, w) * noise_sigma

    noisy_image = np.zeros(temp_image.shape, np.float64)
    if len(temp_image.shape) == 2:
        noisy_image = temp_image + noise
    else:
        noisy_image[:,:,0] = temp_image[:,:,0] + noise
        noisy_image[:,:,1] = temp_image[:,:,1] + noise
        noisy_image[:,:,2] = temp_image[:,:,2] + noise

    return noisy_image

# variant 2
def sp_noise(image,prob=0.05):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

# variant 3
def numpy_noise(image, mean=0.0, std = 1.0):
    # mean = 0.5  # some constant
    # std = 1.0    # some constant (standard deviation)
    noisy_img = image + np.random.normal(mean, std, image.shape)
    return noise_img