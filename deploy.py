from pyinfra.operations import files

files.sync(
    src="./files/",
    dest="/opt/test/",
    user="root",
    group="root",
    mode="0644",
    delete=True,
)
