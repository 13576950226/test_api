import unittest

from htmlrunner import HTMLRunner

if __name__=="__main__":
    suit = unittest.defaultTestLoader.discover(".")
    HTMLRunner(output="../reoprt.html", title="这个是测试报告", description="测试报告描述", tester="CHENAN").run(suit)
