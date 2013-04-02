"""Tests for pytest-bdd-splinter subplugin."""


def test_pytest_assertrepr_compare_called(self, testdir):
        testdir.makeconftest("""
            l = []
            def pytest_assertrepr_compare(op, left, right):
                l.append((op, left, right))
            def pytest_funcarg__l(request):
                return l
        """)
        testdir.makepyfile("""
            def test_hello():
                assert 0 == 1
            def test_check(l):
                assert l == [("==", 0, 1)]
        """)
        result = testdir.runpytest("-v")
        result.stdout.fnmatch_lines([
            "*test_hello*FAIL*",
            "*test_check*PASS*",
        ])
