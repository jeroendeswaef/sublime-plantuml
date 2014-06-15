import sublime_plugin
import sublime
import subprocess

from subprocess import Popen, PIPE, STDOUT

class ConvertUmlCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		urls = []
		placeholder = '//=============='
		full_text = self.view.substr(sublime.Region(0, self.view.size()))

		placeholder_position = full_text.find(placeholder)
		if placeholder_position == -1:
			print("a")
			syntax = full_text
			insert_position = self.view.size()
		else:
			print("b")
			#text_before_fold = full_text.split(placeholder, 1)
			text_before_fold = full_text[:placeholder_position]
			print (text_before_fold)
			print (placeholder_position)
			self.view.erase(edit, sublime.Region(placeholder_position, self.view.size()))
			syntax = text_before_fold

		print ("syntax: %s" % syntax)
		self.view.insert(edit, self.view.size(), placeholder + '\n')
		p = subprocess.Popen(["/usr/bin/java", "-jar", "/opt/plantuml.jar", "-p", "-tutxt"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
		stdout = p.communicate(input=bytes(syntax, 'UTF-8'))[0]

		self.view.insert(edit, self.view.size(), stdout.decode('UTF-8'))
