#include"Header.h"

int DrawPile::isFull()
{ // Acquire current quantity of cards in stack.
	return drawPile.size();
}

bool DrawPile::isEmpty() { // Determine if pile is empty.

	if (drawPile.size() == 0)
		return true;
	else
		return false;
}

bool DrawPile::putCard(Card card) { // Add card to stack.

	drawPile.push(card);
	return true;
}

Card DrawPile::getCard() {

	Card card; 
	if (drawPile.size() > 0) { // If stack currently has cards, acquire one.
		card = drawPile.top();
		drawPile.pop();
		card.visible = true;
	}
	else { // User is pulling from an empty stack.
		card.value = 0;
		card.visible = false;
	}
	return card;
}

bool TargetPile::endOfGame() {

	if (targetPile.size() > 0) { // If target pile contains cards, check if they are Kings of any suite.
		if (targetPile.top().value == 13 || targetPile.top().value == 26 ||
			targetPile.top().value == 39 || targetPile.top().value == 52)
			return true; // If there is a King return true.
	}
	else
		return false; // No king found.
}

bool TargetPile::putCard(Card card) { // Add card to stack.

	targetPile.push(card);
	return true;
}

Card TargetPile::getCard() {

	Card card;
	if (targetPile.size() > 0) { // If stack currently has cards, acquire one.
		card = targetPile.top();
		targetPile.pop();
	}
	else { // User is pulling from an empty stack.
		card.value = 0;
		card.visible = false;
	}
	return card;
}

int TargetPile::isFull() { // Acquire current quantity of cards in stack.

	return targetPile.size();
}

bool TargetPile::isEmpty() { // Determine if pile is empty.

	if (targetPile.size() == 0)
		return true;
	else
		return false;
}

void Hand::setHandPile(stack<Card> & deck, int count) { // Set a single hand pile.

	for (int x = 0; x < count; x++) { // Count ascends while building piles left to right.
		Card card = deck.top();
		if (x == (count - 1)) // If this is the last card to be placed in the pile. Adjust visibility.
			card.visible = true;
		handPile.push_front(card); // Add card to stack.
		deck.pop(); // Remove card from deck.
	}
}

bool Hand::putCard(Card card){ // Add card to stack.

	handPile.push_front(card);
	return true;
}

Card Hand::getCard() {

	Card card;
	if (handPile.size() > 0) { // If stack currently has cards, acquire one.
		card = handPile.front();
		handPile.pop_front();

	}
	else { // User is pulling from an empty stack.
		card.value = 0;
		card.visible = false;
	}
	return card;
}

int Hand::isFull() { // Acquire current quantity of cards in stack.

	return handPile.size();
}

bool Hand::isEmpty() { // Determine if pile is empty.

	if (handPile.size() == 0)
		return true;
	else
		return false;
}

