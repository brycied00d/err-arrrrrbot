How to hack
===========

Please test your changes locally before pushing / creating pull requests:

1. Install errbot: `pip2 install err` (or `pip`, whichever is your distribution's pip for Python 2.7)
2. Install the dependencies of the plugins you want to use (i.e. BeautifulSoup and requests for err-codebot)
3. Run errbot from the project directory: `err.py -T`

You can also load multiple plugins simultaneously from a parent directory:

    % ls
    err-arrrrrbot/  err-codebot/
    % err.py -Tc err-arrrrrbot
    ...

General information about plugin writing: https://github.com/gbin/err/wiki/plugin-dev