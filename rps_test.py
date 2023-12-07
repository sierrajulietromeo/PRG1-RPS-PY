from rps import rock_paper_scissors

# pip install pytest in the terminal
# pytest -v rps_test.py

def test_1_draw():
    assert( rock_paper_scissors( 'paper', 'paper' ) == "draw" )
    assert( rock_paper_scissors( 'rock', 'rock' ) == "draw" )
    assert( rock_paper_scissors( 'scissors', 'scissors' ) == "draw" )


def test_2_player1wins():
    assert( rock_paper_scissors( 'scissors', 'paper' ) == "player1" )
    assert( rock_paper_scissors( 'paper', 'rock' ) == "player1" )
    assert( rock_paper_scissors( 'rock', 'scissors' ) == "player1" )


def test_3_player2wins():
    assert( rock_paper_scissors( 'rock', 'paper' ) == "player2" )
    assert( rock_paper_scissors( 'scissors', 'rock' ) == "player2" )
    assert( rock_paper_scissors( 'paper', 'scissors' ) == "player2" )


def test_4_RPSLS_Draw():
    assert( rock_paper_scissors( 'lizard', 'lizard' ) == "draw" )
    assert( rock_paper_scissors( 'spock', 'spock' ) == "draw" )
    



