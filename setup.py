from setuptools import setup, find_packages

setup(
    name="secure_seed",
    version="1.0.0",
    author="Nwal",
    author_email="roos1100110022r@gmail.com",
    description="High-entropy seed generator using 10 entropy sources for cryptography and PRNG",
    url="https://github.com/nw117722nw1/SecureSeed-Python",
    packages=find_packages(),
    install_requires=["psutil"],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
