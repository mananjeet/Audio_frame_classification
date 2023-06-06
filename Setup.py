from setuptools import setup

setup(
    name='wav2vec2_audioFrameClassification',
    version='1.0',
    install_requires=[
        'numpy',
        'torch',
        'datasets',
        'transformers',
        'tqdm',
    ],
)
