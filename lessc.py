import sublime
import sublime_plugin
import os
import subprocess
from lessc_opts import lessc_opts


class CompileLessOnSave(sublime_plugin.EventListener):

    def on_post_save(self, view):

        if not view.file_name().endswith('.less'):
            return

        folder_name, file_name = os.path.split(view.file_name())
        args = []

        opts = None
        for path in lessc_opts:
            if folder_name in path and len(folder_name) == (len(path) - 1):
                opts = lessc_opts[path]
                opts['less_path'] = path

        if opts is None:
            view.set_status('less', 'File saved but no LESS configuration found for folder ' + folder_name)
            return

        if os.name == "nt":
            lessc = os.path.dirname(os.path.realpath(__file__)) + '\LESS\windows\lessc.exe'
        else:
            lessc = 'lessc'

        css_path = opts['css_path']
        less_path = opts['less_path']
        args = [lessc, '-x', less_path + 'style.less', css_path + 'style.css']
        subprocess.call(args)
        args = ['java', '-jar', opts['cssembed_path'], css_path + 'style.css', '-o', css_path + 'style_base64.css']
        subprocess.call(args)
        os.remove(css_path + 'style.css')
        os.rename(css_path + 'style_base64.css', css_path + 'style.css')
        view.set_status('less', 'File saved and LESS compiled forfolder ' + folder_name)
