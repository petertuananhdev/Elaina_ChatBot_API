from setuptools import setup

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(name='elainaapi',
      author='The DT',
      url='https://github.com/duongtuan303030/elainaapi',
      version="0.0.1",
      packages=["elainaapi"],
      description='A Python wrapper Elaina api API',
      include_package_data=True,
      install_requires=requirements,
      python_requires='>=3.8.0',
)
