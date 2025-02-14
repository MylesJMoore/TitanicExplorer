# Titanic Explorer

A Flask web application that explores and visualizes the Titanic dataset, including statistical summaries and an interactive age distribution graph. Users can filter the dataset by passenger class, survival status, and gender.

## Features

- **Dynamic Data Summary**: Displays key statistics for filtered data.
- **Age Distribution Graph**: Visualizes the distribution of ages among passengers.
- **Interactive Filters**: Allows users to filter the dataset by class, survival status, and gender.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MylesJMoore/TitanicExplorer.git
   cd titanic_explorer
   ```
2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
3. Install the required packages:
   pip install -r requirements.txt
4. Run the application:
   python app.py
5. Visit http://127.0.0.1:5000/ in your browser.

## Usage

- Use the filter form on the homepage to view filtered Titanic data.
- The summary statistics will update based on your filters.
- The age distribution graph will also update dynamically.

## Contributing

1. Fork the repository.
2. Create a new branch (git checkout -b feature-name).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-name).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
