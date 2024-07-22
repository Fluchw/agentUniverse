# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/4/8 20:58
# @Author  : jerry.zzw 
# @Email   : jerry.zzw@antgroup.com
# @FileName: server_application.py

# from agentuniverse.agent_serve.web.web_booster import start_web_server
from agentuniverse.agent_serve.web.court_web_booster import start_web_server
from agentuniverse.base.agentuniverse import AgentUniverse
# from law_app.app.bootstrap.court_web_booster import start_web_server


class ServerApplication:
    """
    Server application.
    """

    @classmethod
    def start(cls):
        # AgentUniverse().start()
        AgentUniverse().start(config_path='../../law_config/law_config.toml')
        start_web_server()


if __name__ == "__main__":
    ServerApplication.start()
