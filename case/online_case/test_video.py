# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   auto_web_GUI
# FileName:     video_test
# Author:      Soozi
# Datetime:    2023/4/9 22:31
# Description：测试类命名以 Test 开头，用例方法以 test 开头,测试的关键在于断言assert
# -----------------------------------------------------------------------------------
import pytest
from process import Recording_full


class TestOnlineRecorder(Recording_full.RecordPage):

    def test_auto_recorder(self, ):

        pass
