#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <unordered_map>

using namespace std;

int main(int argc, char *argv[]){

    unordered_map<string, int> mp;

    mp["red"] = 12;
    mp["green"] = 13;
    mp["blue"] = 14;

    // open file
    fstream f(argv[1]);

    // error check
    if(!f.is_open()){
        cout << "file not available" << endl;
        return -1;
    }

    // some variables to fill each iteration
    string line;
    int ans = 0;
    int r, b, g;

    // id is just # of game, so this value is just incremented each line
    int id = 1;

    // iterate through each line
    while(getline(f, line)){
        
        // split line by ':', not needed
        line = line.substr(line.find(':')+1);

        // iterate through each case of semicolon
        stringstream ss(line);
        string val, col;

        // check if possible by iterating through each val, color pair
        bool POSSIBLE = true;
        cout << "ID: " << id << endl;
        while(ss >> val >> col){
            if(max(mp[col], mp[col.substr(0, col.size()-1)]) < stoi(val)){
                POSSIBLE = false;
                break;
            }
        }

        // only add ID if possible
        if(POSSIBLE){
            ans += id;
        }

        // go to next line
        id++;
    }


    cout << ans << endl;

    return 0;
}