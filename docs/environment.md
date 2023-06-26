# Project Environment
```bash
# Python 3.9.7
conda create -n perspective python=3.9
conda activate perspective
# pytorch 1.10.0 with CUDA 11.3  (see torch.version.cuda)
# conda install pytorch=1.10.0 torchvision torchaudio cudatoolkit=11.3 -c pytorch

# conda install -c conda-forge openexr-python openexr
sudo apt-get install libopenexr-dev
sudo apt-get install openexr
pip install OpenEXR --user 
#  
# openexr build on linux (# -> ref : https://stackoverflow.com/questions/45601949/install-openexr-in-python-doesnt-work) 

# Detectron2
pip install 'git+https://github.com/facebookresearch/detectron2.git'
# others
pip install gitpython opencv-contrib-python albumentations pyequilib==0.3.0 skylibs timm mmcv h5py tensorboard setuptools==59.5.0
# mvcc build on linux (# -> https://mmcv.readthedocs.io/en/latest/get_started/build.html 
) 
# install local packages
cd perspectiveField
pip install -e .
cd ..
```