#pragma once
#include <iostream>
#include <deque> // Used for hand piles.
#include <stack> // Used for all other piles.
using namespace std;

// Fix the use of inheritance? 
// Encountering C2663 and C2662 Compiler errors when attempting to alter contents of derived class stacks.
class Pile {

	protected:

		int topCard;

	public:

		virtual int isFull() const = 0;
		virtual bool isEmpty() const = 0;

		// Used as a means to add card to a stack. Compatiblity checking will happen
		// within this function. 
		virtual bool putCard(int card) const = 0;

		// Use as a means to remove cards from a stack. If the card was deemed incompatible with
		// the destination stack, utilize putCard method to add card back to stack.
		virtual int getCard() const = 0;
};

struct Card { // Card class will be used to construct 52 cards.

	int value = 0; // Actual face value of card 1 - 52.
	bool visible = false; // Visibility of card.
};

class DrawPile { // Will be a total of one DrawPile object.

	private:

		stack<Card> drawPile; // Draw pile stack that will contain all cards cycled in from deck.

	public:

		bool putCard(Card card); // Ability to add cards to the stack.
		Card getCard(); // Removal of card from a stack.

		int isFull(); // Checking current quantity of cards in stacks.
		bool isEmpty(); // Check if stack is empty.
};

class TargetPile { // Total of 4 TargetPile objects.

	private:

		stack<Card> targetPile; // Will contain cards of one suite starting at one and ascending to King.

	public:

		bool endOfGame(); // Checks if there is currently a King in the stack.

		bool putCard(Card card); // Ability to add cards to the stack.
		Card getCard(); // Removal of card from a stack.

		int isFull(); // Checking current quantity of cards in stacks.
		bool isEmpty(); // Check if stack is empty.
};

class Hand { // Total of 7 Hand objects.

	private: 

		deque<Card> handPile; // Can potentially contain all suites descending in value. 
							  // If they alter between (Spades, Clubs) and (Hearts, Diamonds).

	public:

		void setHandPile(stack<Card> & deck, int count); // Building of handPile used in initial program start.

		bool putCard(Card card); // Ability to add cards to the stack.
		Card getCard(); // Removal of card from a stack.

		int isFull(); // Checking current quantity of cards in stacks.
		bool isEmpty(); // Check if stack is empty.
};