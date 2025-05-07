from setuptools import setup, find_packages

setup(
    name="qwop-gym",
    version="1.0.1",
    description="A custom Gymnasium-compatible environment for the QWOP game.",
    author="Your Name",
    packages=[
    'qwop_gym',
    'qwop_gym.envs',
    'qwop_gym.envs.v1',
    'qwop_gym.tools',
    'qwop_gym.wrappers',
    ],
    install_requires=[
        'gymnasium~=0.29.1',
        'websockets~=11.0',
        'numpy~=1.24',
        'selenium~=4.11',
        'pillow~=10.0',
        'pygame~=2.5',
        'pyyaml>=6.0',
    ],
    entry_points={
        "gymnasium.envs": [
            "QWOP-v1=qwop_gym.envs.v1.qwop_env:QwopEnv"
        ]
    },
    include_package_data=True,
    python_requires=">=3.8",
)
