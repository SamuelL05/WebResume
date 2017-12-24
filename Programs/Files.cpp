#include<iostream>
#include<vector>
#include<fstream>
#include<stdio.h>
using namespace std;

struct Inventory {

	int ID = 0;
	char description[50];
	int quantity = 0;
	float price = 0.0;
};

Inventory addData(fstream & file, Inventory item);
fstream modifyData(fstream & file);
void searchData(fstream & file);
void displayData(Inventory & item);
int controller(fstream & file);

int main() {

	int exit = 0;
	fstream file("Inventory.txt", ios::in | ios::out | ios::app | ios::binary);
	if (file.fail()) {
		cout << "File failed to open." << endl;
		return 0;
	}
	while (exit == 0)
		exit = controller(file);
	file.close();
	return 0;
}

int controller(fstream & file) {

	int choice = 0;
	Inventory item;

	cout << "Add Data: 1, Search Data: 2, Edit Data: 3, Exit: 4" << endl;
	do {
		cout << "Enter Here: ";
		cin >> choice;
		if (!cin.good()) {
			cin.clear();
			cin.ignore(80, '\n');
			choice = 0;
		}
	} while (choice < 1 || choice > 4);

	switch (choice) {

	case 1:
		addData(file, item);
		break;

	case 2:
		searchData(file);
		break;

	case 3:
		file = modifyData(file);
		break;

	case 4:
		return 1;
		break;
	}
	return 0;
}

fstream modifyData(fstream & file) {

	Inventory item;
	file.seekg(0L, ios::end);
	int byteSize = file.tellg();
	int itemCount = byteSize / sizeof(item);
	vector<Inventory> fileData;
	int entry = 0;

	cout << "Total Entries: " << itemCount << endl;
	do {
		cout << "Entry to modify: ";
		cin >> entry;
		if (!cin.good()) {
			cin.clear();
			cin.ignore(80, '\n');
			entry = 0;
		}
	} while (entry < 1 || entry > itemCount);
	
	for (int x = 0; x < itemCount; x++) {
		file.seekg((sizeof(item) * x), ios::beg);
		file.read(reinterpret_cast<char*>(&item), sizeof(item));
		if (item.ID == entry) {
			item = addData(file, item);
		}
		fileData.push_back(item);
	}
	file.close();
	remove("Inventory.txt");
	fstream newFile("Inventory.txt", ios::in | ios::out | ios::app | ios::binary);

	for (int x = 0; x < itemCount; x++) {
		file.seekp(0L, ios::end);
		item = fileData[x];
		newFile.write(reinterpret_cast<char*>(&item), sizeof(item));		
	}
	return newFile;
}

Inventory addData(fstream & file, Inventory item) {

	bool modifiedData = false;
	file.seekp(0L, ios::end);
	if (item.ID == 0)
		item.ID = static_cast<char>((file.tellp() / sizeof(item)) + 1);
	else
		modifiedData = true;

	cin.ignore(80, '\n');
	do {
		cout << "\nDescription: ";
		cin.getline(item.description, sizeof(item.description));
	} while (sizeof(item.description) == 0);

	do {
		cout << "Quantity: ";
		cin >> item.quantity;
		if (!cin.good()) {
			cin.clear();
			cin.ignore(80, '\n');
			item.quantity = -1;
		}
	} while (item.quantity < 0);

	do {
		cout << "Price: ";
		cin >> item.price;
		if (!cin.good()) {
			cin.clear();
			cin.ignore(80, '\n');
			item.quantity = -1;
		}
	} while (item.price < 0);
	cout << endl;
	if (modifiedData == false)
		file.write(reinterpret_cast<char *>(&item), sizeof(item));
	else
		return item;
}

void searchData(fstream & file) {

	Inventory item;
	int entry = 0;
	file.seekg(0L, ios::end);
	int itemCount = file.tellg() / sizeof(item);

	if (itemCount != 0) {
		cout << "Total Entires: " << itemCount << endl;
		do {
			cout << "Select Entry: ";
			cin >> entry;
			if (!cin.good()) {
				cin.clear();
				cin.ignore(80, '\n');
			}
		} while (entry < 0 || entry > itemCount);
		file.seekg((sizeof(item) * (entry - 1)), ios::beg);
		file.read(reinterpret_cast<char*>(&item), sizeof(item));
		displayData(item);
	}
	else
		cout << "Empty File." << endl;
}

void displayData(Inventory & item) {

	cout << "\nItem ID: " << item.ID << endl;
	cout << "Item Description: " << item.description << endl;
	cout << "Item Quantity: " << item.quantity << endl;
	cout << "Item Price: " << item.price << "\n\n";
}
