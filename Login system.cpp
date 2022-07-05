#include <iostream>
using namespace std;

int main(){
	string command, user, passwordL, username, password;
	int loginT;
	
	cout<<"exit login register"<<endl;
	cout<<"Choose command: ";
	cin >> command;
	
	while(command != "exit"){
		if(command == "register"){
			cout<<"\n\n"<<endl;
			cout<<"Registration"<<endl;
			cout<<"Enter your username: ";
			cin >> user;
			cout<<"Enter your password: ";
			cin >> password;
			
			cout<< "\n\n"<<endl;
			cout << "Registration Successful!"<< endl;
			
			cout<<"\n\n"<<endl;
			cout << "exit login register"<<endl;
			cout<< "Choose command: ";
			
			cin >> command;
			
			loginT = 3;
			
			if(command == "login"){
					while(loginT > 0){
				cout<<"\n\n"<<endl;
				cout<<"Login"<<endl;
				
				cout<<"Username: ";
				cin>> username;
				cout<<"Password: ";
				cin>> passwordL;
				
				if(username == user && passwordL == password){
					cout<<"You have logged in successfully!"<< endl;
					cout<<"Welcome "<<username<<"!";
					
					
				}
				else if(username != user && passwordL == password){
					cout<<"The username you have entered is incorrect."<<endl;
					loginT--;
					cout<<"You have "<<loginT<<" login attempt/s left!"<<endl;
				}
				else if(username == user && passwordL != password){
					cout<<"The password you have entered is incorrect."<< endl;
					loginT--;
					cout<<"You have "<<loginT<<" login attempt/s left!"<<endl;
				}
				else{
					cout<<"Your username and password are incorrect!"<<"\n"<<endl;
					loginT--;
				}
		
			}
			cout <<"You have entered the incorrect details more than 3 times."<<endl;
			cout<<"You have been blocked out of your account!"<<endl;
			break;	
		}
			
	}
	
}
return 0;
}
