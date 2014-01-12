#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # We want to be able to use --settings for our own end.
    settings = "gplusdemo"
    xs = [x for x in sys.argv if x.startswith("--settings=")]
    if xs:
        settings = xs[0].replace("--settings=", "")
        sys.argv.remove(xs[0])
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "%s.settings" % settings)
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
