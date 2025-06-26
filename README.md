# Last.fm Data Analysis with PySpark

## Overview

This project analyzes Last.fm listening data using PySpark to gain insights into user listening habits, popular artists, and more. It's designed as a portfolio project as an initial step in data engineering, big data processing, and data analysis using PySpark.

## Technologies Used

- PySpark
- Python
- Docker (optional)
- PowerShell (for running the job on Windows)

## Setup

### Prerequisites

- Python 3.6+
- Apache Spark
- `pip`

### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd rka-last-fm-data
    ```

2.  Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1.  **Environment Variables:**

    Set these environment variables in your `.env` file or directly in your system's environment variables. The `.env` file should be in the root directory of the project. Example `.env` file:

    ```
    DATA_DIR=<dir with data files>
    ```

## Usage

1.  **Running the PySpark Job:**

    To run the PySpark job, use the provided `run-python-job.ps1` script (for Windows) or run the script directly using `spark-submit` (for other platforms).

    **On Windows:**

    ```powershell
    .\run-python-job.ps1
    ```

2.  **Analyzing Data:**

    The `last-fm-analyze-main.py` script uses data from the Last.fm files, processes it using PySpark, and outputs:

    - Top artists listened by country users.
    - Top songs listened by country users.

## Data Sources

- [Last.fm Data](http://ocelma.net/MusicRecommendationDataset/lastfm-1K.html): To obtain the data files.

## Project Structure

```
rka-last-fm-data/
├── .env                    # Environment variables
├── .gitignore              # Specifies intentionally untracked files that Git should ignore
├── docker-compose.yml      # Docker compose configuration file (if using Docker)
├── last-fm-analyze-main.py # Main PySpark script for data analysis
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
└── run-python-job.ps1      # PowerShell script to run the PySpark job on Windows
```
