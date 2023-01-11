import setuptools
from src.WaBach import __version__

setuptools.setup(
    name="WaBach",
    version=__version__,
    description="Implementation of the Weyl tensor and the Bach tensor into Gravipy",
    url="",
    author="Simon Knoska",
    author_email="knoskas@gmail.com",
    license="BSD",
    packages=["src/WaBach"],
    include_package_data=True,
    install_requires=["GraviPy == 0.2.0"],
    platforms="any",
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Physics",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)