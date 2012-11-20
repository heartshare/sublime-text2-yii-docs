#!/usr/bin/python

import sublime
import sublime_plugin


class YiidocsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        for region in self.view.sel():
            word = self.view.word(region)
            if not word.empty():
                url = "http://www.yiiframework.com/search/?type=api-suggest&q=%s" % self.view.substr(word)
                sublime.active_window().run_command('open_url', {"url": url})
