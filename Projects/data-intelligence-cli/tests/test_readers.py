
import csv

from app.readers import read_csv


def test_read_csv(tmp_path):
    csv_file = tmp_path / "employees.csv"

    with csv_file.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "age", "department", "salary"],
        )
        writer.writeheader()
        writer.writerow({
            "name": "Alice",
            "age": "25",
            "department": "IT",
            "salary": "50000",
        })

    employees = read_csv(str(csv_file))

    assert len(employees) == 1
    assert employees[0]["name"] == "Alice"
    assert employees[0]["salary"] == "50000"
