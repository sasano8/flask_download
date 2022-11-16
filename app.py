from flask import (
    Flask,
    stream_with_context,
    Response,
)
import numpy as np
from urllib import parse


app = Flask("download")

DIR_PATH = "contents"
FILE_NAME = "mydata.npz"

with open(DIR_PATH + "/" + FILE_NAME, "wb") as f:
    arr = [np.arange(5), np.arange(5)]
    np.savez(f, *arr)


@app.route("/download", methods=["GET"])
def download():
    def iter_data():
        with open(DIR_PATH + "/" + FILE_NAME, "rb") as f:
            while True:
                buf = f.read(1)
                if not buf:
                    break

                yield buf

    return Response(
        stream_with_context(iter_data()),
        content_type="application/octet-stream",
        headers={
            "Content-Disposition": f"attachment; filename={parse.quote(FILE_NAME)}"
        },
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
