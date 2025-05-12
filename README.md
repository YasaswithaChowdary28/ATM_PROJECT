# ATM_PROJECT
# ATM Web Application (Flask + MySQL)

This project is a simple web-based ATM system built using **Flask** (Python) and **MySQL**. It supports operations such as deposits, withdrawals, mini statements, and PIN generation through a multi-step form-based interface.

---

## Features

- **Home Page**: Main navigation to all services.
- **Deposit**: Add money to a given account number.
- **Withdrawal**:
  - Step 1: Validate account number and PIN.
  - Step 2: Enter withdrawal amount and process transaction.
- **Mini Statement**: View basic account info including name, email, and balance after verifying account number and PIN.
- **PIN Generation**:
  - Step 1: Enter account number.
  - Step 2: Set a new PIN if it doesn't already exist.

---

## Technologies Used

- **Python 3**
- **Flask**
- **MySQL (via PyMySQL)**
- **HTML Templates (Jinja2)**

---

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/atm-flask-app.git
    cd atm-flask-app
    ```

2. **Install Required Packages**:
    ```bash
    pip install flask pymysql
    ```

3. **MySQL Database Setup**:
    - Create a database named `atm`.
    - Create a table named `ACCOUNTS` with appropriate fields:
      ```sql
      CREATE TABLE ACCOUNTS (
          USER_ACCNO VARCHAR(20) PRIMARY KEY,
          USER_NAME VARCHAR(100),
          USER_EMAIL VARCHAR(100),
          USER_PIN INT,
          USER_BALANCE INT
      );
      ```

4. **Run the App**:
    ```bash
    python app.py
    ```

    The app will be available at: `http://localhost:5015`

---

## Notes

- Ensure MySQL is running and accessible with the credentials provided in `app.py`.
- Update the `db_config` in `app.py` with your actual DB credentials.
- This is a basic demonstration app and **does not include security best practices** (e.g., password hashing, input validation, SQL injection protection).

---

## License

This project is open-source and free to use for educational purposes.
