
# Robustormer:

This is a modified version of the original [Restormer](https://github.com/swz30/Restormer) repository.
The modifications include the implementation of a penalization term to enhance the model's performance by penalizing the loss function based on specific conditions.


## Introduction
Restormer is an efficient transformer model designed for high-resolution image restoration tasks such as denoising, super-resolution, and deblurring.
This modified version, named Robustormer, introduces a penalization term to further improve the model's performance by ensuring that the final output is valid.

The current implementaion of Robustormer only uses the Gaussian denoising task from Restormer.
## Penalization Term

The penalization term \(P\) is calculated based on the condition:

$$ P = \max\left(0,\|\text{gt}-\text{y}\|_k - 0.5 \times \|\text{gt} - \text{lq}\|_k \right) $$

Where:
-  $lq$ is the low-quality (noisy) input image.
- $gt$ is the ground truth (clean) image.
- $y$ is the output of the denoising model.
- $ \| \cdot \|_k $ denotes the $ \ell_k $ norm.
- $k$ is the order of the norm (default is 1 because the original training loss is $\ell_1$ loss).

The penalization term is applied to the loss function as follows:

$$
\text{loss} = \text{original\_loss} + (\lambda P \times \text{original\_loss})
$$

Where:
- $\lambda$ is the weight of the penalization term (default is 1).
- $original\_loss$ is the original loss function (e.g., pixel-wise $\ell_1$ loss).


## Installation

To instal the required dependencies follow these steps:
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/robustormer.git
    cd robustormer
    ```

2. **Create and Activate a Conda Environment**:
    ```bash
    conda create -n robustormer python=3.7
    conda activate robustormer
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install BasicSR**:
    ```bash
    python setup.py develop --no_cuda_ext
    ```
# Gaussian Image Denoising 

- [Gaussian Image Denoising](#gaussian-image-denoising)
  * [Training](#training)
  * [Evaluation](#evaluation)

- **Blind Denoising:** One model to handle various noise levels
- **Non-Blind Denoising:** Separate models for each noise level

## Training

- Download training (DIV2K, Flickr2K, WED, BSD) and testing datasets:
    - Using `gdown` run:
      ```
      cd Robustormer/Denoising
      python download_data_gdown.py --data train-test --noise gaussian
      ```
    - Or using `go` and `gdrive` following [the packages installation instructions](https://github.com/swz30/Restormer/blob/main/INSTALL.md#download-datasets-from-google-drive) then run:
    ```
    cd Robustormer/Denoising
    python download_data.py --data train-test --noise gaussian
    ```
- Generate image patches from full-resolution training images, run
```
python generate_patches_dfwb.py
```

- Train Restormer for **grayscale blind** image denoising without penalty:
   - To train the original Restormer without penalty run:
   ```
     cd Robustormer
    ./train.sh Denoising/Options/GaussianGrayDenoising_Restormer.yml
   ```
   - To enalble the penalty training for Roustormer, run:
   ```
     cd Robustormer
    ./train.sh Denoising/Options/GaussianGrayDenoising_Restormer.yml --use_penalization True
   ```

**Note:** The above training scripts use 8 GPUs by default. To use any other number of GPUs, modify [Robustormer/train.sh](../train.sh) and the yaml file defining the training parameters ([Denoising/Options/GaussianGrayDenoising_Restormer.yml](Options/GaussianGrayDenoising_Restormer.yml))

## Evaluation

- Download the pre-trained mode [gauusian_gray_denoising_blind](https://drive.google.com/drive/folders/1Qwsjyny54RZWa7zC4Apg7exixLBo4uF0?usp=sharing) and place it in `./pretrained_models/`

- Download testsets (Set12, BSD68, CBSD68, Kodak, McMaster, Urban100), run 
```
python download_data_gdown.py --data test --noise gaussian
```
