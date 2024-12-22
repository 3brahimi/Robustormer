import os
import shutil
import argparse

### Google drive IDs ######
SIDD_train = '1UHjWZzLPGweA9ZczmV8lFSRcIxqiOVJw'
SIDD_val   = '1Fw6Ey1R-nCHN9WEpxv0MnMqxij-ECQYJ'      
SIDD_test  = '11vfqV-lqousZTuAit1Qkqghiv_taY0KZ'      
DND_test   = '1CYCDhaVxYYcXhSfEVDUwkvJDtGxeQ10G'      

BSD400    = '1idKFDkAHJGAFDn1OyXZxsTbOSBx9GS8N'
DIV2K     = '13wLWWXvFkuYYVZMMAYiMVdSA7iVEf2fM'
Flickr2K  = '1J8xjFCrVzeYccD-LF08H7HiIsmi8l2Wn'
WaterlooED = '19_mCE_GXfmE5yYsm-HEzuZQqmwMjPpJr'
gaussian_test = '1mwMLt-niNqcQpfN_ZduG9j4k6P_ZkOl0'

def download_and_extract(file_id, output_path, extract_path):
    os.makedirs(output_path, exist_ok=True)
    os.system(f'gdown https://drive.google.com/uc?id={file_id} -O {output_path}/data.zip')
    print(f'Extracting data to {extract_path}...')
    shutil.unpack_archive(f'{output_path}/data.zip', extract_path)
    os.remove(f'{output_path}/data.zip')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download and extract datasets.')
    parser.add_argument('--data', type=str, required=True, help='Datasets to download, separated by hyphens')
    parser.add_argument('--noise', type=str, required=True, help='Type of noise (e.g., real, gaussian)')
    args = parser.parse_args()

    noise = args.noise

    for data in args.data.split('-'):
        if noise == 'real':
            if data == 'train':
                print('SIDD Training Data!')
                download_and_extract(SIDD_train, 'Datasets/Downloads', 'Datasets/Downloads/SIDD')
                print('SIDD Validation Data!')
                download_and_extract(SIDD_val, 'Datasets', 'Datasets/val')

            if data == 'test':
                print('SIDD Testing Data!')
                download_and_extract(SIDD_test, 'Datasets', 'Datasets/SIDD_test')

        elif noise == 'gaussian':
            if data == 'train':
                print('WaterlooED Training Data!')
                download_and_extract(WaterlooED, 'Datasets/Downloads', 'Datasets/Downloads/WaterlooED')

                print('DIV2K Training Data!')
                download_and_extract(DIV2K, 'Datasets/Downloads', 'Datasets/Downloads/DIV2K')

                print('BSD400 Training Data!')
                download_and_extract(BSD400, 'Datasets/Downloads', 'Datasets/Downloads/BSD400')

                print('Flickr2K Training Data!')
                download_and_extract(Flickr2K, 'Datasets/Downloads', 'Datasets/Downloads/Flickr2K')

            if data == 'test':
                print('Gaussian Denoising Testing Data!')
                download_and_extract(gaussian_test, 'Datasets', 'Datasets/gaussian_test')
                