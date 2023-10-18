#define the base class player
class Player:

  def play(self):
    print("The player is playing cricket.")

    #define the derived class Batsman
    class Batsman(player):

      def play(self):
        print("The batsman is battling.")

        #define the derived class Bowler
        class Bowler(player):

          def play(self):
            print("the Bowler is bowling.")
