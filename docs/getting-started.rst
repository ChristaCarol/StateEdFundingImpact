<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Getting Started Guide</title>
</head>
<body>
    <h1>Getting Started with Educate, Invest, Excel: Budgets & StateEd Priorities</h1>

    <p>Welcome to "Educate, Invest, Excel: Budgets & StateEd Priorities", a comprehensive analysis project focusing on the impact of state funding on academic outcomes. This guide will walk you through the steps needed to set up the project environment and start exploring the data.</p>

    <h2>Prerequisites</h2>
    <p>Before you begin, ensure you have the following installed:</p>
    <ul>
        <li>Python 3.8 or higher</li>
        <li>Jupyter Notebook or JupyterLab</li>
        <li>Git (for version control)</li>
    </ul>

    <h2>Installation</h2>
    <h3>Clone the Repository</h3>
    <p>First, clone the project repository to your local machine using Git:</p>
    <pre><code>git clone https://github.com/yourusername/stateedfundingimpact.git
cd stateedfundingimpact</code></pre>

    <h3>Set Up a Virtual Environment</h3>
    <p>It's recommended to use a virtual environment to manage dependencies:</p>
    <pre><code>python -m venv venv</code></pre>
    <p>Activate the virtual environment:</p>
    <ul>
        <li>On Windows: <code>venv\Scripts\activate</code></li>
        <li>On macOS/Linux: <code>source venv/bin/activate</code></li>
    </ul>

    <h3>Install Dependencies</h3>
    <p>Install the project dependencies using <code>pip</code>:</p>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h2>Exploring the Data</h2>
    <p>The project uses data from the EdFacts 'Adjusted Cohort Graduation Rate' datasets and 'states_all.csv' to analyze the impact of state funding on academic outcomes.</p>
    <ul>
        <li><strong>Data Location</strong>: Once the setup is complete, you can find the data files in the <code>data/raw</code> directory for initial exploration and in <code>data/processed</code> for data that has been cleaned and pre-processed.</li>
        <li><strong>Jupyter Notebooks</strong>: Navigate to the <code>notebooks</code> directory to find Jupyter notebooks used for data exploration and analysis.</li>
    </ul>
    <pre><code>cd notebooks
jupyter notebook</code></pre>
    <p>Start with <code>01_data_preparation.ipynb</code> to see how the data is prepared, followed by <code>02_data_analysis.ipynb</code> for the analysis.</p>

    <h2>Contributing</h2>
    <p>Interested in contributing to the project? Check out <code>CONTRIBUTING.md</code> for guidelines on how to contribute, report issues, or request features.</p>

    <h2>Troubleshooting & Support</h2>
    <p>Encounter any problems? First, check the <code>FAQ.md</code> and <code>TROUBLESHOOTING.md</code> documents for solutions to common issues. If you can't find an answer, please open an issue on the project's GitHub page with a detailed description of the problem.</p>

</body>
</html>
