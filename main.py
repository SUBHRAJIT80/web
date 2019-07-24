#!/usr/bin/env python3

from flask import Flask, render_template
from webproject import app

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5010,
        threaded=True,
        debug=True
    )
