# Full stack application README

This README provides instructions for setting up and running the backend for the "SPM Role Application" project.

## C4 Code Diagram
![C4 Code Diagram](https://github.com/SPM-Job-Portal-App/spm_fullstack/blob/206dc72971c2f83758ddfd47a534f2e204aaa96a/.github/README/SPM%20Code%20Diagram.png?raw=true)

## Prerequisites

Before getting started, ensure you have the following prerequisites installed on your system:

- Docker
- Python (3.6 or higher)
- Virtualenv (for creating a virtual environment)

## Getting Started
### Run the backend
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/SPM-Job-Portal-App/spm_fullstack.git
   ```

2. Change your working directory to the backend directory:
   ```
   cd spm_backend
   ```

3. Start the MySQL database using Docker Compose:
   ```
   docker-compose up
   ```

This command will start the necessary containers for the backend.

3. Create and activate a virtual environment (Mac):
   ```
   python -m venv myenv
   source myenv/bin/activate
   ```

3. Create and activate a virtual environment (Windows):
   ```
   python -m venv myenv
   myenv\Scripts\activate
   ```

4. Install packages required to run application:
   ```
   pip install -r requirements.txt
   ```

5. Run the main backend application:
   ```
   python main.py
   ```

### Run the frontend
1. Change your working directory to the frontend directory:
   ```
   cd spm_frontend
   ```

2. Install package dependencies:
   ```
   npm i
   ```

3. Run the main frontend application:
   ```
   npm run dev
   ```