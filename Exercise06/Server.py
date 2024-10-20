from http.server import BaseHTTPRequestHandler, HTTPServer
import os

from prettytable import PrettyTable
from Exercise05 import (
    get_ranked_students_table,
    get_students_list_table,
    get_subject_scores_table,
    load_from_file,
    transfer_to_students_list
)

PORT_NUMBER = 8080
FILE_PATH = './student02.txt'
INDEX_FILE = 'index.html'


class MyHandler(BaseHTTPRequestHandler):
    '''This class will handle any incoming request from a browser'''

    def __table_to_string(self, table: PrettyTable) -> str:
        table.format = True  # Show border and style eqaul to original PrettyTable
        return table.get_html_string()

    def __do_from_command_get_context(self, command: str) -> str:
        students_raw_list = load_from_file(FILE_PATH)
        self.students_list = transfer_to_students_list(students_raw_list)
        result = None
        if command == "":
            ''' Get the path of index.html relative with Server.py'''
            script_dir = os.path.dirname(os.path.abspath(__file__))
            index_path = os.path.join(script_dir, INDEX_FILE)
            with open(index_path, "r") as index:
                context = index.read()
                return context
        elif command == "1":
            result = get_students_list_table(self.students_list)
        elif command == "2":
            result = get_subject_scores_table(self.students_list)
        elif command == "3":
            result = get_ranked_students_table(self.students_list)

        if result is not None:
            result.format = True  # Show border and style eqaul to original PrettyTable
            return self.__table_to_string(result)
        else:
            return "Nothing"

    def do_GET(self):
        '''Handler for the GET requests'''
        get_command = self.path.split("/")[1]
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        result = self.__do_from_command_get_context(get_command)
        self.wfile.write(result.encode('utf-8'))
        return


try:
    # Create a web server and define the handler to manage the incoming request
    server = HTTPServer(('localhost', PORT_NUMBER), MyHandler)
    print('Started httpserver on port ', PORT_NUMBER)
    # Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
