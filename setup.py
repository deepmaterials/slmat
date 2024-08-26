from setuptools import setup, find_packages

# Function to read the requirements from the requirements.txt file
def load_requirements(filename='requirements.txt'):
    with open(filename, 'r') as file:
        return file.read().splitlines()

setup(
    name='slmat',
    version='2024.8.1',
    author='Kamal Choudhary',
    author_email='writetokamal.1989@gmail.com',
    description='ServerLess Materials Design',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/deepmaterials/slmat',
    packages=find_packages(),
    install_requires=load_requirements(),  # Load dependencies from requirements.txt
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)

