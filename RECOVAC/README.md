## RECOVAC

This folder contains all the initial files required to produce the visualisations shown on the page for the RECOVAC page on the portal.

**Script Archive** - Folder containing older scripts for this project. Largely includes scripts that produce individual plots from the data (typically use the same dataprep files, or data is prepared within the script).

**comorbidity_cases_dataprep.py** - script to prepare data related to the number of covid cases detected in patients with the comorbidities considered (cancer, cardiovascular disease, respiratory disease, and diabetes). Feeds into comorbidity_subplots_wbuttons.py (content of bottom subplot).

**comorbidity_subplots_wbuttons.py** - script to create the plot including subplots of data on COVID-19 cases and vaccination coverage among patients with a comorbidity of interest. The plot includes the buttons shown on the portal page. Uses data from comorbidity_cases_dataprep.py and comorbidity_vaccinecov_dataprep.py.

**comorbidity_vaccinecov_dataprep.py** - script to prepare data related to vaccine coverage among patients with the comorbidities considered (cancer, cardiovascular disease, respiratory disease, and diabetes). Feeds into comorbidity_subplots_wbuttons.py (content of plot subplot).

**requirements.txt** - requirements file showing packages used.

**Swedishpop_ICU_plotwbuttons.py** - script to prepare the data and produce the plot showing the number of admissions to ICU within the general Swedish population. The stacked bar plot is subdivided according to the number of doses a patient received. Buttons are included to choose the ages of patients.

**Swedishpop_vaccinecov_dataprep.py** - script to prepare the data related to vaccine coverage for each dose in the Swedish population. The prepared data is used by Swedishpop_vaccinecov_plotwbuttons.py.

**Swedishpop_vaccinecov_plotwbuttons.py** - script to produce the plot showing the vaccine coverage among the Swedish population. The data is subdivided according to the number of doses a patient received. Buttons are included to choose patient age range and whether or not to align the plots.