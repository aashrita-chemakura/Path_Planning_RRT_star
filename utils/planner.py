'''
@file: planner.py
@breif: Abstract class for planner
@author: Winter
@update: 2023.1.17
'''
import math
from abc import abstractmethod, ABC
from .env import Node,Map
from .plot import Plot

class Planner(ABC):
    def __init__(self, start: tuple, goal: tuple, env: Map) -> None:
        # plannig start and goal
        self.start = Node(start, start, 0, 0)
        self.goal = Node(goal, goal, 0, 0)
        # environment
        self.env = env
        # graph handler
        self.plot = Plot(start, goal, env)

    # def dist(self, node1: Node, node2: Node) -> float:
    #     return math.hypot(node2.current[0] - node1.current[0], node2.current[1] - node1.current[1])
    
    # def angle(self, node1: Node, node2: Node) -> float:
    #     return math.atan2(node2.current[1] - node1.current[1], node2.current[0] - node1.current[0])
    

    def dist(self, node1: Node, node2: Node) -> float:
        return math.hypot(node2.x - node1.x, node2.y - node1.y)
    
    def angle(self, node1: Node, node2: Node) -> float:
        return math.atan2(node2.y - node1.y, node2.x - node1.x)

    @abstractmethod
    def plan(self):
        '''
        Interface for planning.
        '''
        pass

    @abstractmethod
    def run(self):
        '''
        Interface for running both plannig and animation.
        '''
        pass