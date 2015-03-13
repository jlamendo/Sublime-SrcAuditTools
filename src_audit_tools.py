import sublime, sublime_plugin
import sys
import os

class CopyWithLineNumbersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = sublime.Window.active_view(sublime.active_window())
        sels = self.view.sel()
        current_file_name = view.file_name()
        ## Change this if you want it to save to file instead of clipboard
        ## also uncomment the first 5 lines of the
        ## save_notes function, and comment the last line.
        notes_path = os.path.realpath(os.readlink(os.environ['HOME'] +'/Desktop'))
        
        # set file name
        if view.file_name():
            max_line_num = self.get_line_num(sels[-1].end())
            max_line_num_len = len(str(max_line_num))
            format_string = "%0" + str(max_line_num_len) + "d: %s\n"
            selection = self.view.line(selection)  # Extend selection to full lines
            first_line_num = self.get_line_num(selection.begin())

            output = "### At [/" + '/'.join(current_file_name.split('/')[-2:]) + "](subl://open?url=file://" + current_file_name + "&line=" + first_line_num + "):\n\n```"
        else:
            output = "### in scratchpad <unsaved>\n\n```\n\n"
        # To print all the line numbers with the same lenght
        max_line_num = self.get_line_num(sels[-1].end())
        max_line_num_len = len(str(max_line_num))
        format_string = "%0" + str(max_line_num_len) + "d: %s\n"
        
        # handle text
        isFollowupSelection = None
        for selection in sels:
            if isFollowupSelection:
                # split multi selections with ---
                output += "---\n"
            else:
                # but not the first one
                isFollowupSelection = True
            # for each selection
            selection = self.view.line(selection)  # Extend selection to full lines
            first_line_num = self.get_line_num(selection.begin())
            lines = self.view.substr(selection).split("\n")  # Considers all line breaks
            for i, line in enumerate(lines):
                output += format_string % (first_line_num + i, line)
        output += "\n```\n\n"
        # send to clipboard
        return self.save_notes(notes_path, output)
    
    def get_line_num(self, point):
        return self.view.rowcol(point)[0] + 1
    
    def save_notes(self, path, notes):
        #fh = open(path + "/notes.md", "a")
        #data_out =  notes
        #notes.split('\n')
        #fh.write(data_out)
        #return fh.close()
        return sublime.set_clipboard(notes)
