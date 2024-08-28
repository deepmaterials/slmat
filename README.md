# SLMat: ServerLess Materials Design Toolkit

SLMat is a serverless, browser-based toolkit that revolutionizes computational materials science by offering a scalable and efficient alternative to traditional server-based platforms like Google Colab. By eliminating the need for server management and providing persistent setups, SLMat enhances productivity and security, enabling researchers to focus on innovation rather than infrastructure. The toolkit integrates seamlessly with materials databases, supports AI model development, and offers advanced features like AI-guided coding and chatbot integration. With its streamlined workflow, SLMat accelerates production time, promotes reproducibility, and democratizes access to powerful computational resources. This makes SLMat an essential tool for modern materials science, offering a versatile and cost-effective solution for researchers across various domains.

![SLMat schematic](paper/slmat.png)

## Try SLMat Pro

Fill up this [Google form](https://forms.gle/FjrogZFJgTKKY8Y19)



Examples
---------


| Notebooks                                                                                                                                      | SLMat                                                                                                                                        | Descriptions                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Visualizing atoms](https://github.com/deepmaterials/slmat/blob/main/content/Visualization.ipynb)                                                       | [![Open in SLMat]](https://deepmaterials.github.io/slmat/lab?fromURL=https://raw.githubusercontent.com/deepmaterials/slmat/main/content/Visualization.ipynb)                                 | Visualizing atomic structure of face-centered cubic Aluminum.                                                                                                                                                                                                                                                                       |
| [ASE Scaling Test](https://github.com/deepmaterials/slmat/blob/main/content/ASEScalingTest.ipynb)                                                       | [![Open in SLMat]](https://deepmaterials.github.io/slmat/lab?fromURL=https://raw.githubusercontent.com/deepmaterials/slmat/main/content/ASEScalingTest.ipynb)                                 | Examples for analyzing number of atoms vs time taken to simulate copper atoms using ASE and EMT.                                                                                                                                                                                                                                                                       |
| [ASE Ni MD](https://github.com/deepmaterials/slmat/blob/main/content/ASE_Ni_MD.ipynb)                                                  | [![Open in SLMat]](https://deepmaterials.github.io/slmat/lab?fromURL=https://raw.githubusercontent.com/deepmaterials/slmat/main/content/ASE_Ni_MD.ipynb)                            | Examples of running molecular dynamics calculations for Nickel.                                                                                                                                                                                                                                                                                                                                 |
| [Database_analysis](https://github.com/deepmaterials/slmat/blob/main/content/Database_analysis.ipynb)                                                  | [![Open in SLMat]](https://deepmaterials.github.io/slmat/lab?fromURL=https://raw.githubusercontent.com/deepmaterials/slmat/main/content/Database_analysis.ipynb)                            | Examples of loading and analyzing databases such as Materials Project, JARVIS-DFT.                                                                                                                                                                                                                                                                                                                                 |
| [ML Sklearn Steel Fatigue](https://github.com/deepmaterials/slmat/blob/main/content/ML_Sklearn.ipynb)                                                  | [![Open in SLMat]](https://deepmaterials.github.io/slmat/lab?fromURL=https://raw.githubusercontent.com/deepmaterials/slmat/main/content/ML_Sklearn.ipynb)                            | Examples of training machine learning model for steel fatigue using scikit-learn.                                                                                                                                                                                                                                                                                                                                 |


[Open in SLMat]: https://img.shields.io/badge/Open-SLMat-blue



Notes: 

1. If the demo takes longer to start, it maybe due to caching issue, try it in a private/in-cognito tab.
2. Unlike `pip install` in usual jupyterlab, SLMat uses `piplite`/`micropip` package as shown in the demos.
3.  Any publicly available/hosted notebook can be launched with SLMat using `fromURL` function: [`https://deepmaterials.github.io/slmat/lab?fromURL=`](https://deepmaterials.github.io/slmat/lab?fromURL=), e.g., [`https://deepmaterials.github.io/slmat/lab?fromURL=https://raw.githubusercontent.com/knc6/jarvis-tools-notebooks/master/jarvis-tools-notebooks/Analyzing_data_in_the_JARVIS_DFT_dataset.ipynb`](https://deepmaterials.github.io/slmat/lab?fromURL=https://raw.githubusercontent.com/knc6/jarvis-tools-notebooks/master/jarvis-tools-notebooks/Analyzing_data_in_the_JARVIS_DFT_dataset.ipynb)
4.  More detailed documentation development is still work in progress, feedback/suggestions are welcome using [GitHub issues](https://github.com/deepmaterials/slmat/issues/new)


