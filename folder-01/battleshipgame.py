from board import *

class BattleShipGame(object):
  def __init__(self):
    self.player1board = Board()
    self.player2board = Board()

  def player1_attacks_coordinate(self, coordinate):
    self.player2board.receive_attack(coordinate)

  def player2_attacks_coordinate(self, coordinate):
    self.player1board.receive_attack(coordinate)

  def demo01(self):
    self.player1board.deploy_ship(Carrier(Coordinate(2,2)))
    self.player1board.deploy_ship(Battleship(Coordinate(4,4)))
    self.player1board.deploy_ship(Submarine(Coordinate(6,6)))
    self.player1board.deploy_ship(Cruiser(Coordinate(7,7)))
    self.player1board.deploy_ship(Patrol(Coordinate(8,8)))
    
    self.player2board.deploy_ship(Carrier(Coordinate(1,3)))
    self.player2board.deploy_ship(Battleship(Coordinate(3,3)))
    self.player2board.deploy_ship(Submarine(Coordinate(5,3)))
    self.player2board.deploy_ship(Cruiser(Coordinate(7,3)))
    self.player2board.deploy_ship(Patrol(Coordinate(9,3)))

  def demo02(self):
    self.player2board.armada_summary()
    self.player1_attacks_coordinate(Coordinate(3,3))
    print("Player 1's latest attack was: ", self.player2board.latest_received_attack_successful())
    self.player2board.armada_summary()

    self.player2_attacks_coordinate(Coordinate(9,3))
    print("Player 2's latest attack was: ", self.player1board.latest_received_attack_successful())

    self.player2board.armada_summary()
    self.player1_attacks_coordinate(Coordinate(9,3))
    print("Player 1's latest attack was: ", self.player2board.latest_received_attack_successful())
    self.player2board.armada_summary()


a=BattleShipGame()
a.demo01()
a.demo02()