# Summary and skills

This project develops a Convolutional Neural Network (CNN) for classifying plant images into their corresponding plant categories.

The repository includes a Jupyter notebook containing the model development workflow and a Python script for downloading and reorganising the image dataset from Kaggle.

- Python
- Convolutional Neural Networks (CNNs)
- Image classification
- Machine learning model development
- Image dataset preparation
- Training, validation, and testing workflows
- Jupyter Notebook
- Kaggle dataset integration with `kagglehub`
- File and directory manipulation with `pathlib` and `shutil`
- Git and GitHub for version control

# Aim of the project

The aim of this project is to build and evaluate a CNN capable of recognising different types of plants from images.

The project also aims to develop an end-to-end image classification workflow, including:

1. Downloading the plant image dataset from Kaggle.
2. Preparing the images for use in a CNN.
3. Training the model to distinguish between plant categories.
4. Evaluating how well the trained model generalises to unseen images.

The dataset preparation script uses the Kaggle dataset `yudhaislamisulistya/plants-type-datasets` and creates a consolidated `plants_dataset` directory containing one folder per plant class.

# Next steps

Future improvements to the project could include:
- Compare different CNN architectures and model depths.
- Apply transfer learning using pretrained architectures.

# Limitations

- Improve model performance by using schedulers
- Use optuna to more efficiently improve hyper parameters
