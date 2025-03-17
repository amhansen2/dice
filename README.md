# DICE: Data Discovery by Example

## Project Overview
DICE (Data dIsCovery by Example) is a system designed to streamline data discovery by allowing users to input example records and receive relevant datasets. It synthesizes SQL queries based on provided examples and refines search results through user feedback. This approach significantly improves efficiency when working with large datasets that have unstructured or unknown schemas, making data discovery more accessible and intuitive.

## Inspiration
This project is inspired by the demo paper:

El Kindi Rezig, Anshul Bhandari, Anna Fariha, Benjamin Price, Allan Vanterpool, Vijay Gadepally, and Michael Stonebraker. 2021. "DICE: data discovery by example." *Proc. VLDB Endow.* 14, 12 (July 2021), 2819–2822. https://doi.org/10.14778/3476311.3476353

DICE addresses a common problem in data analysis—efficiently locating relevant data within vast and complex datasets. The project aims to implement a functional version of DICE while improving usability and efficiency.

## Project Goals
- Develop a working prototype of DICE with an emphasis on usability.
- Implement an intuitive web interface for enhanced data discovery.
- Improve the UI/UX by making it more interactive and user-friendly.
- Add a feature to upload CSV files as example data for query generation.
- Utilize tools such as Pandas and SQLAlchemy for backend query synthesis.
- Explore and integrate query suggestion tools to enhance the discovery process.

## Features
- **Example-based Query Synthesis**: Users can provide sample records, and the system will generate SQL queries to find similar data.
- **User Feedback Integration**: Refines search results based on iterative feedback.
- **CSV Upload Support**: Users can upload datasets as examples to guide the search process.
- **Interactive Web Interface**: A user-friendly front-end to simplify data exploration.
- **Efficient Data Handling**: Uses Pandas and SQLAlchemy for fast and flexible query execution.

## Technology Stack
- **Frontend**: HTML, CSS, JavaScript (React for UI enhancements)
- **Backend**: Python (Flask or FastAPI)
- **Database**: PostgreSQL or SQLite
- **Data Processing**: Pandas, SQLAlchemy

## Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/DICE.git
   cd DICE
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   python app.py
   ```
5. Access the web interface at `http://localhost:5000`.

## Future Enhancements
- Expand compatibility with more database systems.
- Improve query optimization techniques.
- Implement AI-driven recommendations for refining search queries.
- Enhance visualization of discovered datasets.

## Contributor
Ashlyn Hansen

---
For any questions or contributions, feel free to open an issue or submit a pull request!
