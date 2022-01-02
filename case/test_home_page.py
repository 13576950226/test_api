import os
import sys
sys.path.append(os.getcwd())
from base.base import Base
from script.home_page_script import Homepage


class TestHomepage(Base):

    def test_home_page(self):
        homepage = Homepage(self.driver)
        homepage.location_zhu_hai()
