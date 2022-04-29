from sqlite3 import connect

from django.db import connection


connections = []

class Node:
    def __init__(self, label:int):
        self.connections = connections
        self.label = label

    def setConnections(self, connections:list):
        self.connections = connections