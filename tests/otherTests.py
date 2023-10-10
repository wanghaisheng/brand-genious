from unittest import TestCase
import search.other as other
import sys
from contextlib import contextmanager
from io import StringIO


class TestOther(TestCase):

    # tests if shodan search is returning back the correct link for single flag.
    def test_shodanSearch_shortFlag(self):
        q = "zanussi -sh"
        query = other.Other(q)
        with TestOther.captured_output(self) as (out, err):
            other.Other.shodanSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.shodan.io/search?query=zanussi')

    # tests if whois search is returning back the correct link for big flag.
    def test_shodanSearch_longFlag(self):
        q = "zanussi --shodan"
        query = other.Other(q)
        with TestOther.captured_output(self) as (out, err):
            other.Other.shodanSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.shodan.io/search?query=zanussi')

    # tests output in screen.
    @contextmanager
    def captured_output(self):
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err
