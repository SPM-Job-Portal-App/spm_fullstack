# Backend Application README

This README provides instructions for setting up and running the backend for the "SPM Backend" project.

## Prerequisites

Before getting started, ensure you have the following prerequisites installed on your system:

- Docker
- Python (3.6 or higher)
- Virtualenv (for creating a virtual environment)

## Getting Started

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

4. Run the main backend application:
   ```
   python main.py
   ```