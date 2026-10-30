import sqlite3

DATABASE_NAME = "tax_system_live.db"

def create_database():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Civil servants table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS civil_servants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT UNIQUE NOT NULL,
            full_name TEXT NOT NULL,
            gender TEXT,
            department TEXT,
            position TEXT,
            basic_salary REAL DEFAULT 0,
            housing_allowance REAL DEFAULT 0,
            transport_allowance REAL DEFAULT 0,
            other_allowance REAL DEFAULT 0
        )
    """)

    # Tax evaluations table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tax_evaluations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT NOT NULL,
            evaluation_date TEXT NOT NULL,
            gross_income REAL DEFAULT 0,
            deductions REAL DEFAULT 0,
            taxable_income REAL DEFAULT 0,
            annual_tax REAL DEFAULT 0,
            monthly_paye REAL DEFAULT 0
        )
    """)

    connection.commit()
    connection.close()


def add_civil_servant(
    employee_id,
    full_name,
    gender,
    department,
    position,
    basic_salary,
    housing_allowance,
    transport_allowance,
    other_allowance
):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO civil_servants (
            employee_id,
            full_name,
            gender,
            department,
            position,
            basic_salary,
            housing_allowance,
            transport_allowance,
            other_allowance
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        employee_id,
        full_name,
        gender,
        department,
        position,
        basic_salary,
        housing_allowance,
        transport_allowance,
        other_allowance
    ))

    connection.commit()
    connection.close()


def get_all_civil_servants():
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM civil_servants
        ORDER BY id DESC
    """)

    records = cursor.fetchall()
    connection.close()

    return records
def save_tax_evaluation(
    employee_id,
    evaluation_date,
    gross_income,
    deductions,
    taxable_income,
    annual_tax,
    monthly_paye
):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO tax_evaluations (
            employee_id,
            evaluation_date,
            gross_income,
            deductions,
            taxable_income,
            annual_tax,
            monthly_paye
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        employee_id,
        evaluation_date,
        gross_income,
        deductions,
        taxable_income,
        annual_tax,
        monthly_paye
    ))

    connection.commit()
    connection.close()
def get_all_tax_evaluations():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            tax_evaluations.id,
            tax_evaluations.employee_id,
            civil_servants.full_name,
            tax_evaluations.evaluation_date,
            tax_evaluations.gross_income,
            tax_evaluations.deductions,
            tax_evaluations.taxable_income,
            tax_evaluations.annual_tax,
            tax_evaluations.monthly_paye
        FROM tax_evaluations
        LEFT JOIN civil_servants
        ON tax_evaluations.employee_id = civil_servants.employee_id
        ORDER BY tax_evaluations.id DESC
    """)

    records = cursor.fetchall()

    connection.close()

    return records
def clear_all_records():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM tax_evaluations")
    cursor.execute("DELETE FROM civil_servants")

    cursor.execute(
        "DELETE FROM sqlite_sequence WHERE name IN "
        "('tax_evaluations', 'civil_servants')"
    )

    connection.commit()
    connection.close()    
