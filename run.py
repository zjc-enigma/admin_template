#coding=utf-8
import sys
from app import app





if __name__ == "__main__":
    #app.run(debug=True, host="0.0.0.0", port=5666)
    app.run(port=6666, threaded=True)
