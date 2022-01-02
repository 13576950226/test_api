import os
import sys
sys.path.append(os.getcwd())
from nose_parameterized import parameterized
from base.base import Base
from script.login_script import Login_script


class Login(Base):
    data = [("13576950226", "CH1d69958an+.")]

    @parameterized.expand(data)
    def test_login(self, username, password):
        login = Login_script(self.driver)
        login.login_way(username, password)


