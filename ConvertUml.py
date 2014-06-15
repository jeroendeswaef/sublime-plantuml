import sublime_plugin
import sublime
import subprocess

from subprocess import Popen, PIPE, STDOUT

class ConvertUmlCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		urls = []
		self.full_text = self.view.substr(sublime.Region(0, self.view.size()))

		p = subprocess.Popen(["/usr/bin/java", "-jar", "/opt/plantuml.jar", "-p", "-tutxt"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
		stdout = p.communicate(input=bytes('A -> Z', 'UTF-8'))[0]
		self.view.insert(edit, self.view.size(), stdout.decode('UTF-8'))
