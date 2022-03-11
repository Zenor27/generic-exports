from data import generate_users, generate_addresses
from exports.user import export_users


def main():
    # FIXME: uncomment the following lines to generate a database file
    # generate_users(COUNT=100000)
    # generate_addresses()
    file = export_users()
    with open("users.xlsx", "wb") as f:
        file_content = file.read()
        f.write(file_content)


if __name__ == "__main__":
    main()
