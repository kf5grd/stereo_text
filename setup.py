from setuptools import setup

setup(
    name='stereo_text',
    version='0.1',
    py_modules=['cli', 'stereo_text'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        stereo_text=cli:cli
    ''',
)
