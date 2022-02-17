# Remember - storing secrets in plaintext is potentially unsafe. Consider using
# something like https://cloud.google.com/secret-manager/docs/overview to help keep
# secrets secret.
db_user = os.environ["DB_USER"]
db_pass = os.environ["DB_PASS"]
db_name = os.environ["DB_NAME"]
db_host = os.environ["DB_HOST"]

# Extract port from db_host if present,
# otherwise use DB_PORT environment variable.
host_args = db_host.split(":")
if len(host_args) == 1:
    db_hostname = db_host
    db_port = os.environ["DB_PORT"]
elif len(host_args) == 2:
    db_hostname, db_port = host_args[0], int(host_args[1])

pool = sqlalchemy.create_engine(
    # Equivalent URL:
    # postgresql+pg8000://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
    sqlalchemy.engine.url.URL.create(
        drivername="postgresql+pg8000",
        username=db_user,  # e.g. "my-database-user"
        password=db_pass,  # e.g. "my-database-password"
        host=db_hostname,  # e.g. "127.0.0.1"
        port=db_port,  # e.g. 5432
        database=db_name  # e.g. "my-database-name"
    ),
    **db_config
)
