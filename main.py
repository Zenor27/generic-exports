from data import generate_users, generate_addresses
from exports.user import export_users
from profiler import profile_context


def main():
    # FIXME: uncomment the following lines to generate a database file
    # generate_users(COUNT=100000)
    # generate_addresses()
    file = export_users()
    with open("users.xlsx", "wb") as f:
        file_content = file.read()
        if isinstance(file_content, str):
            file_content = file_content.encode("utf-8")
        f.write(file_content)


if __name__ == "__main__":
    main()
