from yahtzee import YahtzeeGame
from die import Die
import pytest


def test_is_yahtzee_when_all_dice_matches():
    # Arrange: Skapa en YahtzeeGame-instans och tärningar
    game = YahtzeeGame()
    for die in game.dice:
        die.value = 6  # Alla tärningar sätts till samma värde

    # Act: Kontrollera Yahtzee
    result = game.check_yahtzee()

    # Assert: Kontrollera att Yahtzee detekteras
    assert result is True, "Yahtzee should be detected when all dice match."


def test_is_not_yahtzee_when_all_dice_not_matching_each_other():
    # Arrange: Skapa en YahtzeeGame-instans och tärningar
    game = YahtzeeGame()
    for die in game.dice:
        die.value = 6  # Alla tärningar sätts till samma värde
    game.dice[0].value = 2  # En tärning ändras till ett annat värde

    # Act: Kontrollera Yahtzee
    result = game.check_yahtzee()

    # Assert: Kontrollera att Yahtzee inte detekteras
    assert result is False, "Yahtzee should not be detected when dice values differ."


if __name__ == "__main__":
    pytest.main()
