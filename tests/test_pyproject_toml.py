import unittest
import tomllib
import osbot_github_actions
from osbot_github_actions.utils.Version     import Version
from osbot_utils.utils.Files                import path_combine

class test_pyproject_toml(unittest.TestCase):

    def setUp(self):
        path_pyproject_toml = path_combine(osbot_github_actions.path, "../pyproject.toml")
        with open(path_pyproject_toml, 'rb') as file:
            self.pyproject_data = tomllib.load(file)

    def test_tool_poetry(self):
        tool_poetry = self.pyproject_data.get('tool', {}).get('poetry', {})
        assert tool_poetry['name'                ] == "osbot_github_actions"
        assert tool_poetry['version'             ] == Version().value()
        assert tool_poetry['description'         ] == "OWASP Security Bot - GitHub Actions"
        assert "Dinis Cruz <dinis.cruz@owasp.org>" in  tool_poetry['authors']
        assert tool_poetry['license'             ] == "MIT"
        assert tool_poetry['readme'              ] == "README.md"
        assert tool_poetry['homepage'            ] == "https://github.com/owasp-sbot/OSBot-GitHub-Actions"
