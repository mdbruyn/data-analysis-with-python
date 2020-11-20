# Data Analysis with Python Projects

This repository contains **my** solutions for the projects of the python course [Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/) from [freeCodeCamp](https://www.freecodecamp.org/).

In some projects there are also Jupyter Notebook.

## Note

The solutions in this repository are made with `Python 3.9.0`.

## Installation

```bash
git clone git@github.com:ueberBrot/data_analysis_with_python.git

# default name when no other is given
cd <data_analysis_with_python>

poetry install
```

Alternative you can use any other virtual environment e.g. pythons `venv`:

```bash
git clone git@github.com:ueberBrot/data_analysis_with_python.git

# default name when no other is given
cd <data_analysis_with_python>

# use .venv or any name you want
python3 -m venv .venv # python -m venv .venv on a Windows machine

source ./.venv/bin/activate #  .\.venv\Scripts\activate on a Windows machine

pip3 install -r ./requirements.txt # pip install -r .\requirements.txt on a Windows machine
```

If you don't want to try it out locally you can use the `repl.it` links to **my** hosted project solutions.

## [Mean-Variance-Standard Deviation Calculator](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator)

Link to **my** project solution [click me](mean_Variance_standard_deviation_calculator/)

Link to **my** `repl.it` [click me](https://repl.it/@ueberBrot/mean-variance-standard-deviation-calculator#README.md)

## [Demographic Data Analyzer](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/demographic-data-analyzer)

Link to **my** project solution [click me](demographic_data_analyser/)

Link to **my** `repl.it` [click me](https://repl.it/@ueberBrot/demographic-data-analyzer#README.md)

## [Medical Data Visualizer](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer)

**Note:**

One of the tests always failed. It seems it has todo with the version of `matplotlib`. I had to manually change the version in the `poetry.lock` file to version 3.2.2 for the test to work. The problem is known on freeCodeCamp and I found the [solution also in the forum](https://forum.freecodecamp.org/t/medical-data-visualizer-heatmap-values-test-fail/414880/2?).

Link to **my** project solution [click me](medical_data_visualizer/)

Link to **my** `repl.it` [click me](https://repl.it/@ueberBrot/medical-data-visualizer#README.md)

## [Page View Time Series Visualizer](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/page-view-time-series-visualizer)

Link to **my** project solution [click me](page_view_time_series_visualizer/)

Link to **my** `repl.it` [click me](https://repl.it/@ueberBrot/page-view-time-series-visualizer#README.md)
