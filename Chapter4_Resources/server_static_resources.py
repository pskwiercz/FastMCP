from pathlib import Path
from fastmcp import FastMCP
from fastmcp.resources import (
    TextResource,
    BinaryResource,
    FileResource,
    HttpResource,
    DirectoryResource,
)

mcp = FastMCP("file-server")

# Text resource
text_resource = TextResource(
    uri="resource://hello",
    name="Hello Resource",
    text="Hello from FastMCP!"
)
mcp.add_resource(text_resource)

# Binary resource
binary_resource = BinaryResource(
    uri="resource://binary",
    name="Binary Resource",
    data=b"\x01\x02\x03\x04\x05",
    mime_type="application/octet-stream",
)
mcp.add_resource(binary_resource)

# File resource
example_file = Path("./example.txt").resolve()
example_file.write_text("This text comes from a file.\n")

file_resource = FileResource(
    uri=f"file://example",
    name="Example File",
    path=example_file,
    mime_type="text/plain",
)
mcp.add_resource(file_resource)

# HTTP resource
http_resource = HttpResource(
    uri="resource://site",
    name="Google.com Homepage",
    url="https://www.google.com/",
)
mcp.add_resource(http_resource)

# Directory resource
data_dir = Path("./data").resolve()
data_dir.mkdir(exist_ok=True)
(data_dir / "a.txt").write_text("File A")
(data_dir / "b.txt").write_text("File B")

directory_resource = DirectoryResource(
    uri="resource://data", name="Data Directory", path=data_dir, recursive=False
)
mcp.add_resource(directory_resource)


if __name__ == "__main__":
    mcp.run()